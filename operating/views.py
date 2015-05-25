from detection.models import Excuse, Panel, UISubMenu, UIMainMenu, Tabel
from django.shortcuts import render, get_object_or_404
from detection.views import view_template
from guardmaster import common as Common
from operating.bbrr.api import ServerSocket
from detection.value_format import ValueFormat
from django.http import HttpResponseRedirect
from operating.models import Server
from pprint import pprint
import time

# Create your views here.


def get_all_rank_list(panel_id):
    if Common.E_RANKNAME_LIST is None:
        Common.E_RANKNAME_LIST = Tabel.get_enum(panel_id, Common.E_RANKNAME)
    return Common.E_RANKNAME_LIST


def params_by_uid(server, uid):
    ss = ServerSocket(server.ip, server.port)
    ret = ss.get_player_account(uid=uid)
    if ret['result'] != 0:
        return None, None, None
    uin = ret['uin']
    ret = ss.get_player_world_info(uin)
    world_info = ret['world_info']
    if len(world_info) == 0:
        return None, None, None
    world_id = filter(lambda x: x['uid'] == uid, world_info)
    world_id = Common.first(world_id)['world_id']
    return ss, uin, world_id


def get_player_base_info(server, panel_id, uid):
    (ss, uin, world_id) = params_by_uid(server, uid)
    if ss is None:
        return None
    ret = ss.get_player_base_info(uid, world_id)
    ret['uin'] = uin
    ret['world_id'] = world_id
    building_info = ss.get_player_building_and_package(uid, world_id)
    if building_info['result'] != 0:
        return ret
    ret['building_data'] = building_info['building_info']['building_data']
    ret['package_data'] = building_info['building_info']['package_data']
    player_pve_info = ss.get_player_pve_info(uid, world_id)
    if player_pve_info['result'] != 0:
        return ret
    ret['pve_info'] = player_pve_info['pve_info']
    ret['hero_endless_info'] = player_pve_info['hero_endless_info']

    rank_list = get_all_rank_list(panel_id)
    rank_list = map(lambda x: {
            'rank_name': x['EnumDes'],
            'rank_id': x['EnumCd'],
            'rank_info': ss.get_rank_pos(uid, world_id, x['EnumCd']),
        }, rank_list)
    ret['rank_list'] = rank_list
    return ret


def send_mail(server, uid, title, content):
    (ss, uin, world_id) = params_by_uid(server, uid)
    if ss is None:
        return None
    ret = ss.send_mail(
        [uid],
        world_id,
        {
            'mail_title': title,
            'mail_content': content,
            'mail_interval': 60*60*24*7,
        },
        []
    )
    return ret


@Common.competence_required
def notify(request, panel_id, url=Common.URL):
    t = "operating/notify.html"
    d = view_template(request, panel_id, url)
    return render(request, t, d)


@Common.competence_required
def mail(request, panel_id, url=Common.URL):
    t = "operating/mail.html"
    d = view_template(request, panel_id, url)
    panel = get_object_or_404(Panel, pk=panel_id)
    d['servers'] = panel.server_set.all()
    return render(request, t, d)


@Common.competence_required
def single(request, panel_id, url=Common.URL):
    t = "operating/single.html"
    d = view_template(request, panel_id, url)
    panel = get_object_or_404(Panel, pk=panel_id)
    d['servers'] = panel.server_set.all()
    if request.method == 'GET':
        return render(request, t, d)
    if request.method == 'POST':
        server_id = int(request.POST['server'])
        uid = int(request.POST['uid'])
        server = get_object_or_404(Server, pk=server_id)
        ret = get_player_base_info(server, panel_id, uid)
        d['player'] = ret
        d['server_id'] = server_id
        d['uid'] = uid
        return render(request, t, d)
    return render(request, t, d)


@Common.competence_required
def contact(request, panel_id, url=Common.URL):
    t = "operating/contact.html"
    d = view_template(request, panel_id, url)
    panel = get_object_or_404(Panel, pk=panel_id)
    d['servers'] = panel.server_set.all()
    return render(request, t, d)


@Common.competence_required
def contact_reply(request, panel_id, issue_id):
    url = 'contact'
    t = "operating/contact.html"
    d = view_template(request, panel_id, url)
    panel = get_object_or_404(Panel, pk=panel_id)
    sub_menu = Common.get_user_sub_menu(request.user, url)
    d['servers'] = panel.server_set.all()
    issue = Tabel.contact_select(sub_menu, panel, {'id': issue_id})
    if not issue:
        return HttpResponseRedirect('/')
    v = ValueFormat(sub_menu.get_col_map_vals('col_type'), panel_id)
    issue = Common.kvs(sub_menu.get_col_map_vals('col_name'), v.execute(issue))
    issue = Common.first(issue)
    d['issue'] = issue
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        server = get_object_or_404(Server, hostname=issue['hostname'])
        if title and len(title) < 30 and content and len(content) < 256:
            ret = send_mail(server, issue['uid'], title, content)
            vals = (
                issue_id,
                title,
                content,
                time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())),
                request.user.username,
                '0'
            )
            if ret['result'] == 0:
                Tabel.contact_insert(panel, vals)
    reply = Tabel.contact_reply_select(panel, issue_id)
    d['reply'] = reply
    return render(request, t, d)
