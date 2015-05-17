from detection.models import Excuse, Panel, UISubMenu, UIMainMenu, Tabel
from django.shortcuts import render, get_object_or_404
from detection.views import view_template
from guardmaster import common as Common
from operating.bbrr.api import ServerSocket
from operating.models import Server
from pprint import pprint

# Create your views here.


def get_player_base_info(server, uid):
    ss = ServerSocket(server.ip, server.port)
    ret = ss.get_player_account(uid=uid)
    if ret['result'] != 0:
        return None
    uin = ret['uin']
    ret = ss.get_player_world_info(uin)
    world_info = ret['world_info']
    if len(world_info) == 0:
        return None
    world_id = filter(lambda x: x['uid'] == uid, world_info)
    world_id = Common.first(world_id)['world_id']
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
        ret = get_player_base_info(server, uid)
        d['player'] = ret
        d['server_id'] = server_id
        d['uid'] = uid
        return render(request, t, d)
    return render(request, t, d)
