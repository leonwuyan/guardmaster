from detection.models import Excuse, Panel, UISubMenu, UIMainMenu, Tabel
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from operating.singlecontrol import SingleControl
from detection.value_format import ValueFormat
from detection.views import view_template
from guardmaster import common as Common
from operating.models import Server
from pprint import pprint
import json


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
        sc = SingleControl(server, uid, panel_id, request.user.username)
        ret = sc.base_info()
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
            sc = SingleControl(server, issue['uid'], panel_id, request.user.username)
            ret = sc.send_mail(title, content)
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
    sc = SingleControl(server, uid, panel_id, request.user.username)
    ret = {}
    second_param = 0
    if type == 'add':
        second_param = int(request.POST['type_id'])
        ret = sc.add_attr(second_param)
    if type == 'recharge':
        ret = sc.add_vip_level()
    if type == 'dungeon':
        second_param = int(request.POST['dungeon_id'])
        ret = sc.unlock_dungeon(second_param)
    if type == 'kick':
        ret = sc.kick()
    if type == 'chat_ban':
        second_param = int(request.POST['time'])
        ret = sc.chat_ban(second_param)
    if type == 'account_ban':
        second_param = int(request.POST['time'])
        ret = sc.account_ban(second_param)
    if ret['result'] == 0:
        s = type + "|" + str(second_param)
        sc.log(s)
    ret = {'result': ret['result']}
    ret = json.dumps(ret, ensure_ascii=False)
    return HttpResponse(ret, content_type='application/json')