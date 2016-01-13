from detection.models import Excuse, Panel, UISubMenu, UIMainMenu, Tabel
from operating.models import Server
from django.shortcuts import render, get_object_or_404
from detection.views import view_template, view_template_base
from guardmaster import common as Common
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic import View
from deployment.tasks import upload_version, inherit_version, get_client_id
from deployment.models import *
from deployment.version import Version
from deployment.control import server_control, make_list_file
from django.utils import timezone
import json


def get_version(user, panel_id, hostname, platform, channel, url='upload', version=None):
    panel = get_object_or_404(Panel, pk=panel_id)
    sub_menu = Common.get_user_sub_menu(user, url)
    request_get = {
        'hostname': hostname,
        'platform': platform,
        'channel': channel,
        'is_valid': '1',
    }
    if url == 'inherit':
        request_get['start'] = str(get_client_id(panel, version.app()))
        request_get['end'] = str(get_client_id(panel, str(version)))
        ret = Tabel.get_versions(sub_menu, panel, request_get)
        return ret
    else:
        if url == 'app':
            request_get['upt_typ'] = platform + '_app'
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
    d['url'] = url
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
            app_url = request.POST.get('app_url')
            if app_url:
                if app_url == 'inherit':
                    inherit_v = Version(
                        request.POST['inherit_a'],
                        request.POST['inherit_b'],
                        request.POST['inherit_c'],
                        request.POST['inherit_d'],
                    )
                    inherit_hostname_id = int(request.POST['inherit_hostname'])
                    inherit_hostname = get_object_or_404(HostName, pk=inherit_hostname_id)
                    inherit_platform = request.POST['inherit_platform']
                    inherit_channel = request.POST['inherit_channel']
                    if not inherit_v.is_app():
                        d['message'] = 2
                        return render(request, t, d)
                else:
                    if not version.is_app():
                        d['message'] = 2
                        return render(request, t, d)
            else:
                tmp = get_version(
                    request.user,
                    panel_id,
                    hostname.label,
                    platform,
                    channel)
                old_version = Version(tmp['a'], tmp['b'], tmp['c'], tmp['d'])
                if version < old_version or version.is_app():
                    d['message'] = 2
                    return render(request, t, d)
        except Exception as e:
            d['message'] = 2
            return render(request, t, d)

        server = get_object_or_404(Server, pk=server_id)
        if app_url == 'inherit':
            inherit_version.delay(
                panel, server, inherit_hostname, inherit_platform,
                inherit_channel, inherit_v, request.user,
                get_version(
                        request.user,
                        panel_id,
                        hostname.label,
                        platform,
                        channel,
                        url,
                        version))
        else:
            upload_version(
                panel,
                server,
                hostname,
                platform,
                channel,
                version,
                request.user,
                app_url)
        d['message'] = 1
        return HttpResponseRedirect(
            reverse('deployment:patch', args=(panel_id, url)))
    return render(request, t, d)


def version(request, panel_id, hostname_id, platform, channel, version):
    hostname = get_object_or_404(HostName, pk=hostname_id)
    tmp = get_version(
        request.user, panel_id, hostname.label, platform, channel, version)
    ret = json.dumps(tmp, ensure_ascii=False)
    return HttpResponse(ret, content_type='application/json')


@Common.competence_required
def config(request, panel_id, url):
    t = "deployment/config.html"
    d = view_template_base(request, panel_id, url)
    panel = get_object_or_404(Panel, pk=panel_id)
    sco = ServerConfigOrder.objects.filter(panel=panel)[:20]
    ciwp = CIWP.objects.filter(panel=panel)
    databin = DataBin.objects.filter(panel=panel)
    processserver = ProcessServer.objects.filter(panel=panel)
    d['sco'] = sco
    d['ciwp'] = ciwp
    d['databin'] = databin
    d['processserver'] = processserver
    if request.method == 'POST':
        label = request.POST.get('label', 'None')
        version = request.POST.get('version')
        ciwp_id = int(request.POST.get('ciwp'))
        db = request.POST.getlist('databin')
        ps = request.POST.getlist('processserver')
        hs = request.POST.getlist('hotstart')
        hs_free = request.POST.getlist('hotstart_free')
        sco = ServerConfigOrder(
            label=label,
            ciwp_id=ciwp_id,
            version=version,
            date=timezone.now(),
            user=str(request.user),
            panel=panel
            )
        sco.save()
        if make_list_file(sco, db, ps, hs, hs_free):
            d['message'] = '0'
        else:
            d['message'] = '1'
    return render(request, t, d)


@Common.competence_required
def control(request, panel_id, url):
    t = "deployment/control.html"
    d = view_template_base(request, panel_id, url)
    panel = get_object_or_404(Panel, pk=panel_id)
    tmp = panel.server_set.all()
    d['url'] = url
    d['servers'] = filter(lambda x: x.server_type != 'update', tmp)
    if url == 'version':
        d['servers'] = filter(lambda x: x.server_type == 'dir', tmp)
    d['ciwps'] = panel.ciwp_set.all()
    d['servercontrolworkorders'] = panel.servercontrolworkorder_set.all()[:20]
    if request.method == 'POST':
        server_id = int(request.POST['server'])
        if url == 'server':
            fn = '_deployment'
            package = {
                'panel': panel,
                'server': get_object_or_404(Server, pk=server_id),
                'parameter1': request.POST['stage'],
                'parameter2': request.POST['release'],
                'parameter3': request.POST['ciwp'],
                'parameter4': request.POST['version'],
                'user': request.user,
            }
        if url == 'version':
            fn = '_change_version'
            commitvers = "{0}:{1}".format(
                request.POST['commitvers_from'], request.POST['commitvers_to'])
            gmvers = "{0}:{1}".format(
                request.POST['gmvers_from'], request.POST['gmvers_to'])
            package = {
                'panel': panel,
                'server': get_object_or_404(Server, pk=server_id),
                'parameter1': request.POST['platform'],
                'parameter2': request.POST['chgtype'],
                'parameter3': commitvers,
                'parameter4': gmvers,
                'user': request.user,
            }
        server_control(fn, package)
        return HttpResponseRedirect(
            reverse('deployment:control', args=(panel_id, url)))
    return render(request, t, d)


@Common.competence_required
def pre_update(request, panel_id, url):
    t = "deployment/preupdate.html"
    d = view_template_base(request, panel_id, url)
    panel = get_object_or_404(Panel, pk=panel_id)
    sub_menu = Common.get_user_sub_menu(request.user, url)
    if request.method == 'POST':
        if request.POST.get('submit') == 'del':
            Tabel.delete(sub_menu, panel)
        if request.POST.get('submit') == 'add':
            vals = [request.POST.get('ip'), request.POST.get('channel')]
            Tabel.pre_update_insert(panel, vals)
    ip_channel = Tabel.select(sub_menu, panel)
    ips = Ip.objects.filter(panel=panel)
    channels = Channel.objects.filter(panel=panel)
    d['ip_channels'] = ip_channel
    d['channels'] = channels
    d['ips'] = ips
    return render(request, t, d)
