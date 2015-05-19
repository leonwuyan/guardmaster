from itertools import chain
from django.http import HttpResponseRedirect


URL = 'total'
ENUM = 'enum'
E_BUILDINGID = 'BuildingId'
E_CHANNELID = 'ChannelID'
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
DATE_FORMAT_ERROR = 'date format error'
TIME_FORMAT_ERROR = 'time format error'
FORMAT_ERROR = 'format error'


def kv(k, v):
    return dict(zip(k, v))


def kvs(k, vs):
    return map(lambda x: kv(k, x), vs)


def get_user_panels(user):
    groups = user.groups.all()
    panels = map(lambda x: x.panel_set.all(), groups)
    panels = apply(chain, panels)
    panels = map(lambda x: x.get_id_label(), panels)
    return panels


def get_user_menus(user):
    groups = user.groups.all()
    main_menus = map(lambda x: x.uimainmenu_set.all(), groups)
    main_menus = apply(chain, main_menus)
    main_menus = map(lambda x: x.get_sub_menu_all(), main_menus)
    return main_menus


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
        menus = get_user_menus(user)
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
    ret = filter(lambda x: x.get('EnumCd') == enum_cd, iterable)
    return first(ret, {}).get('EnumDes', default)
