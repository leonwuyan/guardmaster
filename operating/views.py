from detection.models import Excuse, Panel, UISubMenu, UIMainMenu, Tabel
from django.views.decorators.http import require_http_methods
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from detection.views import view_template
from guardmaster import common as Common
from operating.bbrr.api import ServerSocket
from detection.value_format import ValueFormat
from django.http import HttpResponseRedirect
from operating.models import Server
from pprint import pprint
import json

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
    world_info = Common.first(filter(lambda x: x['uid'] == uid, world_info))
    world_id = world_info['world_id']
    return ss, uin, world_id, world_info


def get_player_base_info(server, panel_id, uid):
    (ss, uin, world_id, world_info) = params_by_uid(server, uid)
    if ss is None:
        return None
    ret = ss.get_player_base_info(uid, world_id)
    ret['uin'] = uin
    ret['world_id'] = world_id
    ret['world_info'] = world_info
    recharge = ss.get_player_total_recharge(uid, world_id)
    if recharge['result'] == 0:
        ret['total_recharge'] = recharge['total_recharge']
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
    (ss, uin, world_id, world_info) = params_by_uid(server, uid)
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


def add_attr(server, uid, type_id, res_id=46, count=100000):
    (ss, uin, world_id, world_info) = params_by_uid(server, uid)
    if ss is None:
        return {'result': -1}
    ret = ss.change_player_attr(uid, uin, world_id, type_id, res_id, count)
    return ret


def add_vip_level(server, uid, count=10000):
    (ss, uin, world_id, world_info) = params_by_uid(server, uid)
    if ss is None:
        return {'result': -1}
    ret = ss.change_player_vip_level(uid, world_id, count)
    return ret


def unlock_dungeon(server, uid, dungeon_id):
    (ss, uin, world_id, world_info) = params_by_uid(server, uid)
    if ss is None:
        return {'result': -1}
    ret = ss.change_player_unlock_dungeon(uid, uin, world_id, dungeon_id)
    return ret


def kick(server, uid):
    (ss, uin, world_id, world_info) = params_by_uid(server, uid)
    if ss is None:
        return {'result': -1}
    ret = ss.kick_player(uid, uin, world_id)
    return ret


def chat_ban(server, uid, time):
    (ss, uin, world_id, world_info) = params_by_uid(server, uid)
    if ss is None:
        return {'result': -1}
    ret = ss.ban_player_chat(uid, time, uin, world_id)
    return ret


def account_ban(server, uid, time):
    (ss, uin, world_id, world_info) = params_by_uid(server, uid)
    if ss is None:
        return {'result': -1}
    ret = ss.lock_player(uid, time)
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
                Common.now(),
                request.user.username,
                '0'
            )
            if ret['result'] == 0:
                Tabel.contact_insert(panel, vals)
    reply = Tabel.contact_reply_select(panel, issue_id)
    d['reply'] = reply
    return render(request, t, d)


@require_http_methods(["POST"])
@Common.competence_required
def change_single(request, panel_id, url, type):
    uid = int(request.POST['uid'])
    server_id = int(request.POST['server_id'])
    server = get_object_or_404(Server, pk=server_id)
    ret = {}
    if type == 'add':
        type_id = int(request.POST['type_id'])
        ret = add_attr(server, uid, type_id)
    if type == 'recharge':
        ret = add_vip_level(server, uid)
    if type == 'dungeon':
        dungeon_id = int(request.POST['dungeon_id'])
        ret = unlock_dungeon(server, uid, dungeon_id)
    if type == 'kick':
        ret = kick(server, uid)
    if type == 'chat_ban':
        time = int(request.POST['time'])
        ret = chat_ban(server, uid, time)
    if type == 'account_ban':
        time = int(request.POST['time'])
        ret = account_ban(server, uid, time)
    ret = {'result': ret['result']}
    ret = json.dumps(ret, ensure_ascii=False)
    return HttpResponse(ret, content_type='application/json')
