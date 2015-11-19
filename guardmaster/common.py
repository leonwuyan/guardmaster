from itertools import chain
from django.http import HttpResponseRedirect
from datetime import *
import time
import hotshot
import os
import time
import settings
import tempfile

URL = 'contact'
ENUM = 'enum'
CONTACT_REPLY = 'contact_reply'
MAX_CLIENT_ID = 'max_client_id'
CLIENT_ID = 'client_id'
E_BUILDINGID = 'BuildingId'
E_CHANNELID = 'ChannelID'
E_PACKAGECHANNEL = 'PackgeChannel'
E_CHGREASON = 'ChgReason'
E_CHGTYPE = 'ChgType'
E_COMPAYCODE = 'CompayCode'
E_DUNTYPE = 'DunType'
E_EQUIPID = 'EquipID'
E_ITEMNAME = 'ItemName'
E_RANKNAME = 'RankName'
E_RESTYPE = 'ResType'
E_ROLEID = 'RoleID'
E_SKILLID = 'SkillID'
E_ZONEID = 'ZoneID'
E_PAYCHANNEL = 'PayChannel'
E_CHATTYPE = 'ChatType'
E_USERSTATUS = 'UserStatus'
E_BUILDINGID_LIST = None
E_CHANNELID_LIST = None
E_CHGREASON_LIST = None
E_CHGTYPE_LIST = None
E_COMPAYCODE_LIST = None
E_DUNTYPE_LIST = None
E_EQUIPID_LIST = None
E_ITEMNAME_LIST = None
E_RANKNAME_LIST = None
E_RESTYPE_LIST = None
E_ROLEID_LIST = None
E_SKILLID_LIST = None
E_ZONEID_LIST = None
E_PAYCHANNEL_LIST = None
E_PACKAGECHANNEL_LIST = None
E_CHATTYPE_LIST = None
E_USERSTATUS_LIST = None
DATE_FORMAT_ERROR = 'date format error'
TIME_FORMAT_ERROR = 'time format error'
FORMAT_ERROR = 'format error'

try:
    PROFILE_LOG_BASE = settings.BASE_DIR
except:
    PROFILE_LOG_BASE = tempfile.gettempdir()


def kv(k, v):
    return dict(zip(k, v))


def kvs(k, vs):
    return map(lambda x: kv(k, x), vs)


def now(t=None):
    if t:
        return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    else:
        return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(t))


def datetime2string(t, tz=0):
    ts = time.mktime(t.timetuple()) + tz
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(ts))


def datetime2ts(t, tz=0):
    ts = time.mktime(t.timetuple()) + tz
    return int(ts)


def string2ts(t, tz=0):
    if t:
        ts = time.mktime(time.strptime(t, '%Y-%m-%d %H:%M:%S')) + tz
    else:
        ts = 0
    return int(ts)


def get_user_panels(user):
    groups = user.groups.all()
    panels = map(lambda x: x.panel_set.all(), groups)
    panels = apply(chain, panels)
    panels = map(lambda x: x.get_id_label(), panels)
    return panels


def get_user_menus(user, panel_id):
    groups = user.groups.all()
    main_menus = map(lambda x: x.uimainmenu_set.all(), groups)
    main_menus = apply(chain, main_menus)
    main_menus = filter(lambda x: x.is_in_panels(panel_id), main_menus)
    main_menus = map(lambda x: x.get_sub_menu_all(), main_menus)
    return main_menus


def get_user_sub_menu(user, url):
    groups = user.groups.all()
    main_menus = map(lambda x: x.uimainmenu_set.all(), groups)
    main_menus = apply(chain, main_menus)
    sub_menus = map(lambda x: x.uisubmenu_set.all(), main_menus)
    sub_menus = apply(chain, sub_menus)
    sub_menu = first(filter(lambda x: x.url == url, sub_menus))
    return sub_menu


def get_panel_response_mail(panel):
    servers = panel.server_set.all()
    responsemails = map(lambda x: x.responsemail_set.all()[:20], servers)
    responsemails = apply(chain, responsemails)
    return responsemails


def get_panel_response_all_mail(panel):
    servers = panel.server_set.all()
    responseallmails = map(lambda x: x.responseallmail_set.all()[:20], servers)
    responseallmails = apply(chain, responseallmails)
    return responseallmails


def competence_required(function):
    def wrap(request, *args, **kwargs):
        user = request.user
        if not user.is_authenticated():
            return HttpResponseRedirect('/')

        panel_id = int(kwargs.get('panel_id'))
        if panel_id is None:
            return HttpResponseRedirect('/')

        panels = get_user_panels(user)
        pt = False
        for p in panels:
            if p.get('id') == panel_id:
                pt = True
        if not pt:
            return HttpResponseRedirect('/')

        url = kwargs.get('url', URL)
        menus = get_user_menus(user, panel_id)
        mt = False
        for m in menus:
            for s in m.get('sub_menu'):
                if s.get('url') == url:
                    mt = True
        if not mt:
            return HttpResponseRedirect('/')
        return function(request, *args, **kwargs)

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap


def first(iterable, default=None):
    if iterable:
        for item in iterable:
            return item
    return default


def filter_enum(iterable, enum_cd, default=None):
    ret = filter(lambda x: x.get('EnumCd') == str(enum_cd), iterable)
    return first(ret, {}).get('EnumDes', default)


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def profile(log_file):
    if not os.path.isabs(log_file):
        log_file = os.path.join(PROFILE_LOG_BASE, 'log/' + log_file)

    def _outer(f):
        def _inner(*args, **kwargs):
            (base, ext) = os.path.splitext(log_file)
            base = base + "-" + time.strftime("%Y%m%dT%H%M%S", time.gmtime())
            final_log_file = base + ext

            prof = hotshot.Profile(final_log_file)
            try:
                ret = prof.runcall(f, *args, **kwargs)
            finally:
                prof.close()
            return ret

        return _inner
    return _outer
