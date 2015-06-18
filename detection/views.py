from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from detection.models import Excuse, Panel, UISubMenu, UIMainMenu, Tabel
from guardmaster import common as Common
from detection.value_format import ValueFormat
import subprocess
import random
import json
import decimal


def view_init():
    Common.E_BUILDINGID_LIST = None
    Common.E_CHANNELID_LIST = None
    Common.E_CHGREASON_LIST = None
    Common.E_CHGTYPE_LIST = None
    Common.E_COMPAYCODE_LIST = None
    Common.E_DUNTYPE_LIST = None
    Common.E_EQUIPID_LIST = None
    Common.E_ITEMNAME_LIST = None
    Common.E_RANKNAME_LIST = None
    Common.E_RESTYPE_LIST = None
    Common.E_ROLEID_LIST = None
    Common.E_SKILLID_LIST = None
    Common.E_ZONEID_LIST = None


def sh_remote_log(panel, request_get):
    if 'start' not in request_get:
        return
    if 'end' not in request_get:
        return
    if 'server' not in request_get:
        return
    if 'uid' not in request_get:
        return
    path = '/root/bbc_statdb/tools/shells/'
    server = panel.server_set.get(ip=request_get.get('server'))
    cmd = [
        './remote_getuidlog.sh',
        panel.symbol,
        request_get.get('server'),
        server.home,
        server.user,
        request_get.get('start'),
        request_get.get('end'),
        request_get.get('uid')
    ]
    cmd = ' '.join(cmd)
    s = subprocess.Popen(cmd, shell=True, cwd=path)
    s.wait()


def view_template(request, panel_id, url):
    excuse = random.choice(Excuse.objects.all())
    view_init()

    panel = get_object_or_404(Panel, pk=panel_id)
    sub_menu = Common.get_user_sub_menu(request.user, url)
    menus = Common.get_user_menus(request.user)

    table_head = sub_menu.get_col_map_dict(['label'])

    channel_list = Tabel.get_enum(panel_id, Common.E_CHANNELID)
    zone_list = Tabel.get_enum(panel_id, Common.E_ZONEID)

    data = {
        'excuse': excuse,
        'title': sub_menu.label,
        'menus': menus,
        'page': url,
        'panel': panel,
        'table_head': table_head,
        'channels': channel_list,
        'zones': zone_list,
    }

    return data


class DecimalJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return str(o)
        return super(DecimalJSONEncoder, self).default(o)


@Common.competence_required
def json_template(request, panel_id, t_p, url=Common.URL):
    panel = get_object_or_404(Panel, pk=panel_id)
    sub_menu = Common.get_user_sub_menu(request.user, url)
    vf = ValueFormat(sub_menu.get_col_map_vals('col_type'), panel_id)
    ret = None
    if t_p == 'count':
        ret = Tabel.count_select(sub_menu, panel, request.GET)
    if t_p == 'count_without_time':
        ret = Tabel.count_without_time_select(sub_menu, panel, request.GET)
    if t_p == 'count_only_time':
        ret = Tabel.count_only_time_select(sub_menu, panel, request.GET)
    if t_p == 'user_query':
        ret = Tabel.user_qeury_select(sub_menu, panel, request.GET)
    if t_p == 'gang_query':
        ret = Tabel.gang_qeury_select(sub_menu, panel, request.GET)
    if t_p == 'deal_query':
        ret = Tabel.deal_query_select(sub_menu, panel, request.GET)
    if t_p == 'history_query':
        sh_remote_log(panel, request.GET)
        ret = Tabel.history_query_select(sub_menu, panel, request.GET)
    if t_p == 'contact':
        ret = Tabel.contact_select(sub_menu, panel, request.GET)
    if ret is None:
        ret = Tabel.count_select(sub_menu, panel, request.GET)
    ret = vf.execute(ret)
    ret = {'data': ret}
    ret = json.dumps(ret, ensure_ascii=False, cls=DecimalJSONEncoder)
    return HttpResponse(ret, content_type='application/json')


@Common.competence_required
def count(request, panel_id, url=Common.URL):
    t = "detection/count.html"
    d = view_template(request, panel_id, url)
    return render(request, t, d)


@Common.competence_required
def count_without_time(request, panel_id, url=Common.URL):
    t = "detection/count_without_time.html"
    d = view_template(request, panel_id, url)
    return render(request, t, d)


@Common.competence_required
def count_only_time(request, panel_id, url=Common.URL):
    t = "detection/count_only_time.html"
    d = view_template(request, panel_id, url)
    return render(request, t, d)


@Common.competence_required
def user_query(request, panel_id, url=Common.URL):
    t = "detection/user_query.html"
    d = view_template(request, panel_id, url)
    return render(request, t, d)


@Common.competence_required
def gang_query(request, panel_id, url=Common.URL):
    t = "detection/gang_query.html"
    d = view_template(request, panel_id, url)
    return render(request, t, d)


@Common.competence_required
def deal_query(request, panel_id, url=Common.URL):
    t = "detection/deal_query.html"
    d = view_template(request, panel_id, url)
    return render(request, t, d)


@Common.competence_required
def history_query(request, panel_id, url=Common.URL):
    t = "detection/history_query.html"
    d = view_template(request, panel_id, url)
    panel = get_object_or_404(Panel, pk=panel_id)
    d['servers'] = panel.server_set.all()
    return render(request, t, d)
