from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from detection.models import Excuse, Panel, UISubMenu, UIMainMenu, Tabel
from django.contrib.auth.decorators import login_required
from pprint import pprint
from guardmaster import common as Common
from detection.value_format import ValueFormat
import random
import json


# Create your views here.


def home(request):
    excuse = random.choice(Excuse.objects.all())
    return render(request, "detection/index.html", {'excuse': excuse})


@Common.panel_required
def count(request, panel_id, url=Common.URL):
    excuse = random.choice(Excuse.objects.all())

    panel = get_object_or_404(Panel, pk=panel_id)
    sub_menu = get_object_or_404(UISubMenu, url=url)
    menus = Common.get_user_menus(request.user)

    table_head = sub_menu.get_col_map_dict(['label'])

    channel_list = Tabel.get_list(panel, Common.CHANNEL_LIST)
    zone_list = Tabel.get_list(panel, Common.ZONE_LIST)

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

    return render(request, "detection/count.html", data)


@Common.panel_required
def count_json(request, panel_id, url=Common.URL):
    panel = get_object_or_404(Panel, pk=panel_id)
    sub_menu = get_object_or_404(UISubMenu, url=url)
    vf = ValueFormat(sub_menu.get_col_map_vals('col_type'), panel)

    ret = Tabel.count_select(sub_menu, panel, request.GET)
    ret = vf.execute(ret)
    ret = {'data': ret}
    ret = json.dumps(ret, ensure_ascii=False)
    return HttpResponse(ret, content_type='application/json')


@Common.panel_required
def query(request, panel_id, url=Common.URL):
    excuse = random.choice(Excuse.objects.all())

    panel = get_object_or_404(Panel, pk=panel_id)
    sub_menu = get_object_or_404(UISubMenu, url=url)
    menus = Common.get_user_menus(request.user)

    table_head = sub_menu.get_col_map_dict(['label'])

    channel_list = Tabel.get_list(panel, Common.CHANNEL_LIST)
    zone_list = Tabel.get_list(panel, Common.ZONE_LIST)

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

    return render(request, "detection/count.html", data)


@Common.panel_required
def query_json(request, panel_id, url=Common.URL):
    panel = get_object_or_404(Panel, pk=panel_id)
    sub_menu = get_object_or_404(UISubMenu, url=url)
    vf = ValueFormat(sub_menu.get_col_map_vals('col_type'), panel)

    ret = Tabel.count_select(sub_menu, panel, request.GET)
    ret = vf.execute(ret)
    ret = {'data': ret}
    ret = json.dumps(ret, ensure_ascii=False)
    return HttpResponse(ret, content_type='application/json')
