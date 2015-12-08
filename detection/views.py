from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from detection.models import Excuse, Panel, UISubMenu, UIMainMenu, Tabel
from guardmaster import common as Common
from detection.value_format import ValueFormat
import subprocess
import random
import json
import decimal
import logging
import time


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
    Common.E_PAYCHANNEL_LIST = None
    Common.E_PACKAGECHANNEL_LIST = None
    Common.E_CHATTYPE_LIST = None
    Common.E_USERSTATUS_LIST = None


def _sh(cmd):
    path = '/root/bbc_statdb/tools/shells/'
    spend_time = time.time()
    cmd = ' '.join(cmd)
    s = subprocess.Popen(cmd, shell=True, cwd=path, stdout=subprocess.PIPE)
    retcode = s.wait()
    output = s.communicate()
    spend_time = str(time.time() - spend_time)
    logger = logging.getLogger(__name__)
    logger.info(path + '|' + cmd + '|' + str(retcode) + '|' + spend_time)
    return output


def sh_remote_log(panel, t_p, request_get):
    if 'start' not in request_get:
        return
    if 'end' not in request_get:
        return
    if 'server' not in request_get:
        return
    if 'uid' not in request_get:
        return
    server = panel.server_set.get(ip=request_get.get('server'))
    if t_p == 'history_query':
        cmd = [
            './remote_getuidlog_multi.sh',
            panel.symbol,
            request_get.get('server'),
            server.home,
            server.user,
            request_get.get('start').split(' ')[0],
            request_get.get('end').split(' ')[0],
            request_get.get('uid')
        ]
        _sh(cmd)
    if t_p == 'everyday_history_query':
        cmd = [
            './remote_getuidlog_his.sh',
            panel.symbol,
            request_get.get('uid'),
            request_get.get('start').split(' ')[0],
            'dm'
        ]
        _sh(cmd)
        cmd = [
            './remote_getuidlog_his.sh',
            panel.symbol,
            request_get.get('uid'),
            request_get.get('start').split(' ')[0],
            'gm'
        ]
        _sh(cmd)


def clac_panel_start_date(panel):
    start_date = str(panel.start_date)
    today = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    month_age = time.strftime('%Y-%m-%d', time.localtime(time.time()-2592000))
    ret = {}
    if start_date < month_age:
        ret['start'] = month_age
    else:
        ret['start'] = start_date
    ret['end'] = today
    return ret


def view_template_base(request, panel_id, url):
    excuse = random.choice(Excuse.objects.all())
    view_init()

    panel = get_object_or_404(Panel, pk=panel_id)
    count_date = clac_panel_start_date(panel)
    sub_menu = Common.get_user_sub_menu(request.user, url)
    menus = Common.get_user_menus(request.user, int(panel_id))

    table_head = sub_menu.get_col_map_dict(['label'])

    data = {
        'excuse': excuse,
        'title': sub_menu.label,
        'menus': menus,
        'page': url,
        'panel': panel,
        'table_head': table_head,
        'count_date': count_date,
    }

    return data


def view_template(request, panel_id, url):
    data = view_template_base(request, panel_id, url)

    channel_list = Tabel.get_enum(panel_id, Common.E_CHANNELID)
    pay_channel_list = Tabel.get_enum(panel_id, Common.E_PAYCHANNEL)
    zone_list = Tabel.get_enum(panel_id, Common.E_ZONEID)

    data['channels'] = channel_list
    data['pay_channels'] = pay_channel_list
    data['zones'] = zone_list

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
    if t_p == 'chat_query':
        server_id = int(request.GET['server_id'])
        vf.set_server_id(server_id)
        ret = Tabel.chat_query_select(sub_menu, panel, request.GET)
    if t_p == 'deal_query' or t_p == 'everyday_deal_query':
        ret = Tabel.deal_query_select(sub_menu, panel, request.GET)
    if t_p == 'history_query' or t_p == 'everyday_history_query':
        sh_remote_log(panel, t_p, request.GET)
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
def count_with_pay_channel(request, panel_id, url=Common.URL):
    t = "detection/count_with_pay_channel.html"
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
def everyday_deal_query(request, panel_id, url=Common.URL):
    t = "detection/everyday_deal_query.html"
    d = view_template(request, panel_id, url)
    return render(request, t, d)


@Common.competence_required
def history_query(request, panel_id, url=Common.URL):
    t = "detection/history_query.html"
    d = view_template(request, panel_id, url)
    panel = get_object_or_404(Panel, pk=panel_id)
    d['servers'] = panel.server_set.filter(server_type='dir')
    return render(request, t, d)


@Common.competence_required
def everyday_history_query(request, panel_id, url=Common.URL):
    t = "detection/everyday_history_query.html"
    d = view_template(request, panel_id, url)
    panel = get_object_or_404(Panel, pk=panel_id)
    d['servers'] = panel.server_set.filter(server_type='dir')
    return render(request, t, d)


@Common.competence_required
def chat_query(request, panel_id, url=Common.URL):
    t = "detection/chat_query.html"
    d = view_template(request, panel_id, url)
    chat_type_list = Tabel.get_enum(panel_id, Common.E_CHATTYPE)
    user_status_list = Tabel.get_enum(panel_id, Common.E_USERSTATUS)
    panel = get_object_or_404(Panel, pk=panel_id)
    d['servers'] = panel.server_set.filter(server_type='dir')
    d['chat_type_list'] = chat_type_list
    d['user_status_list'] = user_status_list
    return render(request, t, d)


@Common.competence_required
def online(request, panel_id, url=Common.URL):
    t = "detection/online.html"
    d = view_template(request, panel_id, url)
    cmd = ["cat", "/tmp/online_ios.log"]
    output_ios = _sh(cmd)
    d['output_ios'] = output_ios[0].replace("\n", "<br/>")
    cmd = ["cat", "/tmp/online_37.log"]
    output_37 = _sh(cmd)
    d['output_37'] = output_37[0].replace("\n", "<br/>")
    cmd = ["cat", "/tmp/online_tx.log"]
    output_tx = _sh(cmd)
    d['output_tx'] = output_tx[0].replace("\n", "<br/>")
    return render(request, t, d)
