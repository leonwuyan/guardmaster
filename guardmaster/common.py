from itertools import chain
from django.http import HttpResponseRedirect


URL = 'total'
CHANNEL_LIST = 'channel_list'
ZONE_LIST = 'zone_list'
CHANNEL_ERROR = 'channel id is error'
ZONE_ERROR = 'zone id is error'
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


def panel_required(function):
    def wrap(request, *args, **kwargs):
        user = request.user
        if not user.is_authenticated():
            return HttpResponseRedirect('/')

        url = kwargs.get('url', URL)
        panel_id = int(kwargs.get('panel_id'))
        if panel_id is None:
            return HttpResponseRedirect('/')

        panels = get_user_panels(user)
        for p in panels:
            if p.get('id') == panel_id:
                return function(request, *args, **kwargs)
        return HttpResponseRedirect('/')

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap
