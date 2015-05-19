from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from detection.models import Excuse, Panel, UISubMenu, UIMainMenu, Tabel
from django.contrib.auth.decorators import login_required
from pprint import pprint
from guardmaster import common as Common
from detection.value_format import ValueFormat
import random
import json


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


def view_template(request, panel_id, url):
    excuse = random.choice(Excuse.objects.all())
    view_init()

    panel = get_object_or_404(Panel, pk=panel_id)
    sub_menu = get_object_or_404(UISubMenu, url=url)
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


@Common.competence_required
def json_template(request, panel_id, t_p, url=Common.URL):
    panel = get_object_or_404(Panel, pk=panel_id)
    sub_menu = get_object_or_404(UISubMenu, url=url)
    vf = ValueFormat(sub_menu.get_col_map_vals('col_type'), panel_id)
    ret = None
    if t_p == 'count':
        ret = Tabel.count_select(sub_menu, panel, request.GET)
    if t_p == 'user_query':
        ret = Tabel.user_qeury_select(sub_menu, panel, request.GET)
    if t_p == 'gang_query':
        ret = Tabel.gang_qeury_select(sub_menu, panel, request.GET)
    if t_p == 'deal_query':
        ret = Tabel.deal_query_select(sub_menu, panel, request.GET)
    if ret is None:
        ret = Tabel.count_select(sub_menu, panel, request.GET)
    ret = vf.execute(ret)
    ret = {'data': ret}
    ret = json.dumps(ret, ensure_ascii=False)
    return HttpResponse(ret, content_type='application/json')


@Common.competence_required
def count(request, panel_id, url=Common.URL):
    t = "detection/count.html"
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
