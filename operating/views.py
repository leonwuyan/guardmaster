from detection.models import Excuse, Panel, UISubMenu, UIMainMenu, Tabel
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from django.utils.translation import ugettext as _
from operating.servercontrol import ServerControl
from operating.notifydeployment import NotifyDeployment
from detection.value_format import ValueFormat
from detection.views import view_template
from guardmaster import common as Common
from operating.models import *
from pprint import pprint
import json
import time


def enum_equip_list(panel_id):
    if Common.E_EQUIPID_LIST is None:
        tmp_list = Tabel.get_enum(panel_id, Common.E_EQUIPID)
        tmp_list = map(lambda x: {
            'EnumCd': int(x['EnumCd']), 'EnumDes': x['EnumDes']}, tmp_list)
        tmp_list = sorted(tmp_list, key=lambda x: x['EnumCd'])
        tmp_list = map(lambda x: {
            'EnumCd': str(x['EnumCd']), 'EnumDes': x['EnumDes']}, tmp_list)
        Common.E_EQUIPID_LIST = tmp_list
    return Common.E_EQUIPID_LIST


def enum_item_list(panel_id):
    if Common.E_ITEMNAME_LIST is None:
        tmp_list = Tabel.get_enum(panel_id, Common.E_ITEMNAME)
        tmp_list = map(lambda x: {
            'EnumCd': int(x['EnumCd']), 'EnumDes': x['EnumDes']}, tmp_list)
        tmp_list = sorted(tmp_list, key=lambda x: x['EnumCd'])
        tmp_list = map(lambda x: {
            'EnumCd': str(x['EnumCd']), 'EnumDes': x['EnumDes']}, tmp_list)
        Common.E_ITEMNAME_LIST = tmp_list
    return Common.E_ITEMNAME_LIST


def enum_factor_list(panel_id):
    if Common.E_FACTOR_LIST is None:
        tmp_list = Tabel.get_enum(panel_id, Common.E_FACTOR)
        tmp_list = map(lambda x: {
            'EnumCd': int(x['EnumCd']), 'EnumDes': x['EnumDes']}, tmp_list)
        tmp_list = sorted(tmp_list, key=lambda x: x['EnumCd'])
        tmp_list = map(lambda x: {
            'EnumCd': str(x['EnumCd']), 'EnumDes': x['EnumDes']}, tmp_list)
        Common.E_FACTOR_LIST = tmp_list
    return Common.E_FACTOR_LIST


def enum_package_channel_list(panel_id):
    if Common.E_PACKAGECHANNEL_LIST is None:
        Common.E_PACKAGECHANNEL_LIST = Tabel.get_enum(
            panel_id, Common.E_PACKAGECHANNEL)
    return Common.E_PACKAGECHANNEL_LIST


@Common.competence_required
def notify(request, panel_id, url=Common.URL):
    if 'synchronization' in request.POST:
        t = "operating/synchronization.html"
        d = view_template(request, panel_id, url)
        nd = NotifyDeployment(panel_id, request.user.username)
        d['cdn_urls'] = nd.tojson()
        return render(request, t, d)
    t = "operating/notify.html"
    d = view_template(request, panel_id, url)
    panel = get_object_or_404(Panel, pk=panel_id)
    d['servers'] = panel.server_set.filter(server_type='dir')
    d['notifys'] = panel.notify_set.all()
    d['channels'] = enum_package_channel_list(panel_id)
    d['url'] = url
    if request.method == 'POST':
        nd = NotifyDeployment(panel_id, request.user.username)
        ret = nd.add(request.POST)
        d['message'] = ret
    return render(request, t, d)


@Common.competence_required
def edit_notify(request, panel_id, id):
    if request.method == 'GET':
        t = "operating/notify.html"
        url = 'notify'
        d = view_template(request, panel_id, url)
        panel = get_object_or_404(Panel, pk=panel_id)
        notify = get_object_or_404(Notify, pk=id)
        d['servers'] = panel.server_set.filter(server_type='dir')
        d['notifys'] = panel.notify_set.all()
        d['channels'] = enum_package_channel_list(panel_id)
        d['url'] = url
        notify.start = Common.datetime2string(notify.start, 28800)
        notify.end = Common.datetime2string(notify.end, 28800)
        d['notify'] = notify
        return render(request, t, d)
    if request.method == 'POST':
        notify = get_object_or_404(Notify, pk=id)
        notify.delete()
        ret = 0
        ret = {'result': ret}
        ret = json.dumps(ret, ensure_ascii=False)
        return HttpResponse(ret, content_type='application/json')


@Common.competence_required
def mail(request, panel_id, url=Common.URL):
    t = "operating/mail.html"
    d = view_template(request, panel_id, url)
    panel = get_object_or_404(Panel, pk=panel_id)
    d['servers'] = panel.server_set.filter(server_type='dir')
    d['equips'] = enum_equip_list(panel_id)
    d['items'] = enum_item_list(panel_id)
    d['factors'] = enum_factor_list(panel_id)
    d['responsemails'] = Common.get_panel_response_mail(panel)
    d['url'] = url
    if request.GET.get('result'):
        d['message'] = request.GET.get('result')
    if request.method == 'POST':
        server_id = int(request.POST['server'])
        try:
            u = request.POST['uid'].split(',')
            u = map(lambda x: int(x), u)
            if len(u) == 1:
                uid = u[0]
            if len(u) > 1 and len(u) <= 1000:
                uid = u
            if len(u) > 1000:
                d['message'] = 2
                return render(request, t, d)
        except Exception as e:
            d['message'] = 2
            return render(request, t, d)

        server = get_object_or_404(Server, pk=server_id)
        sc = ServerControl(
            server,
            uid,
            panel_id,
            request.user.username,
            Common.get_client_ip(request))
        ret = sc.send_mail(post=request.POST)
        hrrurl = reverse('operating:mail', args=(panel_id, url)) + '?result=' + str(ret['result'])
        return HttpResponseRedirect(hrrurl)
    return render(request, t, d)


@Common.competence_required
def all_mail(request, panel_id, url=Common.URL):
    t = "operating/all_mail.html"
    d = view_template(request, panel_id, url)
    panel = get_object_or_404(Panel, pk=panel_id)
    d['servers'] = panel.server_set.filter(server_type='dir')
    d['equips'] = enum_equip_list(panel_id)
    d['items'] = enum_item_list(panel_id)
    d['factors'] = enum_factor_list(panel_id)
    d['responseallmails'] = Common.get_panel_response_all_mail(panel)
    if request.GET.get('result'):
        d['message'] = request.GET.get('result')
    if request.method == 'POST':
        server_id = int(request.POST['server'])

        server = get_object_or_404(Server, pk=server_id)
        sc = ServerControl(
            server,
            0,
            panel_id,
            request.user.username,
            Common.get_client_ip(request))
        ret = sc.send_all_mail(request.POST)
        hrrurl = reverse('operating:all_mail', args=(panel_id, url)) + '?result=' + str(ret['result'])
        return HttpResponseRedirect(hrrurl)
    return render(request, t, d)


@Common.competence_required
def single(request, panel_id, url=Common.URL):
    t = "operating/single.html"
    d = view_template(request, panel_id, url)
    panel = get_object_or_404(Panel, pk=panel_id)
    d['servers'] = panel.server_set.filter(server_type='dir')
    d['url'] = url
    if request.method == 'POST':
        server_id = int(request.POST['server'])
        uid = int(request.POST['uid'])
        server = get_object_or_404(Server, pk=server_id)
        sc = ServerControl(
            server,
            uid,
            panel_id,
            request.user.username,
            Common.get_client_ip(request))
        if url == 'single_query_tw':
            ret = sc.base_info_tw()
        else:
            ret = sc.base_info()
        d['player'] = ret
        d['server_id'] = server_id
        d['uid'] = uid
    return render(request, t, d)


@Common.competence_required
def contact(request, panel_id, url=Common.URL):
    t = "operating/contact.html"
    d = view_template(request, panel_id, url)
    panel = get_object_or_404(Panel, pk=panel_id)
    d['servers'] = panel.server_set.filter(server_type='dir')
    return render(request, t, d)


@Common.competence_required
def contact_reply(request, panel_id, issue_id):
    url = 'contact'
    t = "operating/contact.html"
    d = view_template(request, panel_id, url)
    panel = get_object_or_404(Panel, pk=panel_id)
    sub_menu = Common.get_user_sub_menu(request.user, url)
    d['servers'] = panel.server_set.filter(server_type='dir')
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
        server = get_object_or_404(Server, hostname=issue['hostname'], panel=panel)
        if title and len(title) < 30 and content and len(content) < 256:
            sc = ServerControl(
                server,
                int(issue['uid']),
                panel_id,
                request.user.username,
                Common.get_client_ip(request))
            ret = sc.send_mail(title, content)
            vals = (
                issue_id,
                title,
                content,
                Common.now(),
                request.user.username,
                str(Common.first(ret['sucess_result'])['mail_id'])
            )
            if ret['result'] == 0:
                Tabel.contact_insert(panel, vals)
                Tabel.update_contact_status(panel, 1, issue_id)
    reply = Tabel.contact_reply_select(panel, issue_id)
    d['reply'] = reply
    return render(request, t, d)


@Common.competence_required
def contact_status(request, panel_id, issue_id):
    panel = get_object_or_404(Panel, pk=panel_id)
    Tabel.update_contact_status(panel, 2, issue_id)
    ret = 0
    ret = {'result': ret}
    ret = json.dumps(ret, ensure_ascii=False)
    return HttpResponse(ret, content_type='application/json')


@require_http_methods(["POST"])
@Common.competence_required
def change_single(request, panel_id, url, type):
    uid = int(request.POST['uid'])
    server_id = int(request.POST['server_id'])
    server = get_object_or_404(Server, pk=server_id)
    sc = ServerControl(
        server,
        uid,
        panel_id,
        request.user.username,
        Common.get_client_ip(request))
    ret = {}
    log_str = ""
    start_time = time.time()
    is_log = True
    if type == 'add':
        type_id = int(request.POST['type_id'])
        count = int(request.POST['count'])
        ret = sc.add_attr(type_id=type_id, count=count)
        log_str = str(type_id) + "|" + str(count)
    if type == 'recharge':
        count = int(request.POST['count'])
        ret = sc.add_vip_level(count)
        log_str = str(count)
    if type == 'dungeon':
        dungeon_id = int(request.POST['dungeon_id'])
        ret = sc.unlock_dungeon(dungeon_id)
        log_str = str(dungeon_id)
    if type == 'kick':
        ret = sc.kick()
    if type == 'chat_ban':
        spend_time = int(request.POST['time'])
        ret = sc.chat_ban(spend_time)
        log_str = str(spend_time)
    if type == 'account_ban':
        spend_time = int(request.POST['time'])
        ret = sc.account_ban(spend_time)
        log_str = str(spend_time)
    if type == 'kick_ban':
        spend_time = int(request.POST['time'])
        ret = sc.account_ban(spend_time)
        ret = sc.chat_ban(spend_time)
        ret = sc.kick()
    if type == 'off_gang':
        ret = sc.off_gang()
        is_log = False
    if type == 'off_rank':
        ret = sc.off_rank()
        is_log = False
    if type == 'month':
        count = int(request.POST['count'])
        ret = sc.change_month_card_remain_days(count)
        log_str = str(count)
    if ret['result'] == 0:
        s = type + "|" + log_str
        sc.log(s)
    try:
        if is_log:
            db_bool = sc.db_log({
                'type': type,
                'post': request.POST,
                'ret': ret,
                'start_time': start_time,
                'done_time': time.time(),
            })
    except Exception as e:
        print 'e :', e
    ret = {'result': ret['result']}
    ret = json.dumps(ret, ensure_ascii=False)
    return HttpResponse(ret, content_type='application/json')


@Common.competence_required
def rank(request, panel_id, url=Common.URL):
    t = "operating/rank.html"
    d = view_template(request, panel_id, url)
    panel = get_object_or_404(Panel, pk=panel_id)
    d['servers'] = panel.server_set.filter(server_type='dir')
    rank_sc = ServerControl(0, 0, panel_id, request.user.username, 0)
    d['ranks'] = rank_sc.ranks()
    if request.method == 'POST':
        server_id = int(request.POST['server'])
        rank_id = int(request.POST['rank'])
        rank_start = int(request.POST['rank_start'])
        rank_end = int(request.POST['rank_end'])
        world_id = int(request.POST['zone'])
        rank_count = rank_end - rank_start + 1
        server = get_object_or_404(Server, pk=server_id)
        sc = ServerControl(server, 0, panel_id, request.user.username, 0)
        ret = sc.all_rank(world_id, rank_id, rank_start, rank_count)
        d['rank'] = ret
        d['server_id'] = server_id
        d['rank_id'] = rank_id
        d['rank_start'] = rank_start
        d['rank_end'] = rank_end
    return render(request, t, d)


@Common.competence_required
def guard_master_order(request, panel_id, url=Common.URL):
    t = "operating/guard_master_order.html"
    d = view_template(request, panel_id, url)
    panel = get_object_or_404(Panel, pk=panel_id)
    d['servers'] = panel.server_set.filter(server_type='dir')
    d['orders'] = GmOrder.objects.filter(is_work=0)
    if request.GET.get('result'):
        d['message'] = request.GET.get('result')
        d['server_id'] = int(request.GET.get('server_id'))
        d['uid'] = request.GET.get('uid')
    if request.method == 'POST':
        server_id = int(request.POST['server'])
        uid = int(request.POST['uid'])
        server = get_object_or_404(Server, pk=server_id)
        gm_text = request.POST.get('order')
        param = request.POST.getlist('param')
        try:
            param = map(lambda x: int(x), param)
            sc = ServerControl(server, uid, panel_id, request.user.username, 0)
            ret = sc.guard_master_order_copy_gm_text(gm_text, param)
        except Exception as e:
            print e
            urld = '?result={0}&uid={1}&server_id={2}'.format(
                'e', uid, server_id)
            hrrurl = reverse('operating:guard_master_order', args=(panel_id, url)) + urld
            return HttpResponseRedirect(hrrurl)
        if ret['result'] == 0:
            s = gm_text + "|" + str(param)
            sc.log(s)
        urld = '?result={0}&uid={1}&server_id={2}'.format(
            str(ret['result']), uid, server_id)
        hrrurl = reverse('operating:guard_master_order', args=(panel_id, url)) + urld
        return HttpResponseRedirect(hrrurl)
    return render(request, t, d)
