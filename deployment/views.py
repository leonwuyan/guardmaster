from detection.models import Excuse, Panel, UISubMenu, UIMainMenu, Tabel
from operating.models import Server
from django.shortcuts import render, get_object_or_404
from detection.views import view_template, view_template_base
from guardmaster import common as Common
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic import View
from deployment.tasks import _do_sh, upload_patch
from deployment.models import HostName
from deployment.version import Version
import json


def get_version(user, panel_id, hostname, platform, channel):
    url = 'upload'
    panel = get_object_or_404(Panel, pk=panel_id)
    sub_menu = Common.get_user_sub_menu(user, url)
    request_get = {
        'hostname': hostname,
        'platform': platform,
        'channel': channel,
    }
    ret = Tabel.get_last_version(sub_menu, panel, request_get)
    if len(ret) > 0:
        tmp = {
            'a': ret[0][0],
            'b': ret[0][1],
            'c': ret[0][2],
            'd': ret[0][3],
        }
    else:
        tmp = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
    return tmp


@Common.competence_required
def patch(request, panel_id, url=Common.URL):
    t = "deployment/patch.html"
    d = view_template_base(request, panel_id, url)
    panel = get_object_or_404(Panel, pk=panel_id)
    d['servers'] = panel.server_set.filter(server_type='update')
    d['hostnames'] = panel.hostname_set.all()
    d['platforms'] = panel.platform_set.all()
    d['channels'] = panel.channel_set.all()
    d['uploadworkorders'] = panel.uploadworkorder_set.all()[:20]
    if request.method == 'POST':
        server_id = int(request.POST['server'])
        try:
            version = Version(
                request.POST['a'],
                request.POST['b'],
                request.POST['c'],
                request.POST['d'],
            )
            hostname_id = int(request.POST['hostname'])
            hostname = get_object_or_404(HostName, pk=hostname_id)
            platform = request.POST['platform']
            channel = request.POST['channel']
            tmp = get_version(
                request.user,
                panel_id,
                hostname.label,
                platform,
                channel)
            old_version = Version(tmp['a'], tmp['b'], tmp['c'], tmp['d'])
            if version < old_version:
                d['message'] = 2
                return render(request, t, d)
        except Exception as e:
            d['message'] = 2
            return render(request, t, d)

        server = get_object_or_404(Server, pk=server_id)
        upload_patch(
            panel,
            server,
            hostname,
            platform,
            channel,
            version,
            request.user)
        d['message'] = 1
        return HttpResponseRedirect(reverse('deployment:patch', args=(panel_id, url)))
    return render(request, t, d)


def version(request, panel_id, hostname, platform, channel):
    tmp = get_version(request.user, panel_id, hostname, platform, channel)
    ret = json.dumps(tmp, ensure_ascii=False)
    return HttpResponse(ret, content_type='application/json')
