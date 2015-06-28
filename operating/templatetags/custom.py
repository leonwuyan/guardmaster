from django.utils.translation import ugettext_lazy as _
from guardmaster import common as Common
from detection.models import Tabel
from django import template
import datetime
import time
register = template.Library()


def ts2date(timestamp):
    try:
        ts = int(timestamp)
    except ValueError:
        return ""
    return datetime.datetime.fromtimestamp(ts)


def ts2time(timestamp):
    try:
        ts = int(timestamp)
    except ValueError:
        return ""
    if ts == 0:
        return _('Not Time')
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(ts))


def second2time(second):
    try:
        ss = int(second)
    except ValueError:
        return ""
    t = {
        'hour': ss / 3600,
        'minute': (ss % 3600) / 60,
        'second': ss % 60,
    }
    return _("%(hour)s H %(minute)s M %(second)s S") % t


def online(is_online):
    if is_online == 0:
        return _("OFF LINE")
    if is_online == 1:
        return _("ON LINE")
    return ""


def is_range(x, r):
    if x >= r[0] and x <= r[1]:
        return True
    else:
        return False


def filter_list(l, label, v=None, r=None):
    if l is None:
        return None
    if v is not None:
        return filter(lambda x: x[label] == v, l)
    if r is not None:
        return filter(lambda x: is_range(x[label], r), l)
    return None


def equiped(hero_equiped_info, hero_id):
    r = Common.first(filter_list(hero_equiped_info, 'hero_id', hero_id))
    if r:
        return r['equiped_info']
    return None


def reduce_join_list(l, label=None):
    if label is not None:
        l = map(lambda x: x[label], l)
    if len(l) > 0:
        return reduce(lambda x, y: x+y, l)
    return None


def tab_join(tab_info):
    return reduce_join_list(tab_info, 'obj_info')


def novice_dungeon(dungeon_list):
    return filter_list(dungeon_list, 'dungeon_id', None, [2600, 2700])


def normal_dungeon(dungeon_list):
    return filter_list(dungeon_list, 'dungeon_id', None, [0, 1000])


def elite_dungeon(dungeon_list):
    return filter_list(dungeon_list, 'dungeon_id', None, [10000, 11000])


def endless_dungeon(dungeon_list):
    return filter_list(dungeon_list, 'dungeon_id', 1001)


def filter_dungeon(dungeon_list, k):
    if k == '1':
        return novice_dungeon(dungeon_list)
    if k == '2':
        return normal_dungeon(dungeon_list)
    if k == '3':
        return elite_dungeon(dungeon_list)
    if k == '4':
        return endless_dungeon(dungeon_list)
    return None


def filter_dungeon_label(dungeon_label, k):
    if k == '1':
        return _('Novice Dungeon List')
    if k == '2':
        return _('Normal Dungeon List')
    if k == '3':
        return _('Elite Dungeon List')
    if k == '4':
        return _('Endless Dungeon List')
    return None


def enum_hero(hero_id, panel_id):
    if Common.E_ROLEID_LIST is None:
        Common.E_ROLEID_LIST = Tabel.get_enum(panel_id, Common.E_ROLEID)
    return Common.filter_enum(Common.E_ROLEID_LIST, hero_id)


def enum_equip(equip_id, panel_id):
    if Common.E_EQUIPID_LIST is None:
        Common.E_EQUIPID_LIST = Tabel.get_enum(panel_id, Common.E_EQUIPID)
    return Common.filter_enum(Common.E_EQUIPID_LIST, equip_id)


def enum_item(item_id, panel_id):
    if Common.E_ITEMNAME_LIST is None:
        Common.E_ITEMNAME_LIST = Tabel.get_enum(panel_id, Common.E_ITEMNAME)
    return Common.filter_enum(Common.E_ITEMNAME_LIST, item_id)


def enum_restype(res_type_id, panel_id):
    if Common.E_RESTYPE_LIST is None:
        Common.E_RESTYPE_LIST = Tabel.get_enum(panel_id, Common.E_RESTYPE)
    return Common.filter_enum(Common.E_RESTYPE_LIST, res_type_id)


def enum_building(building_id, panel_id):
    if Common.E_BUILDINGID_LIST is None:
        Common.E_BUILDINGID_LIST = Tabel.get_enum(panel_id, Common.E_BUILDINGID)
    return Common.filter_enum(Common.E_BUILDINGID_LIST, building_id)


def rank_val(rank_id, pos):
    val = [
        ('', '',),
        ('', '',),
        (_("PvP Win Times"), _("PvP Total Times"),),
        (_("Endless Score"), _("Endless Floor"),),
        (_("Gang Score"), _("Gang History Score"),),
        (_("Achievement Score"), _("Achievement Times"),),
        (_("Fight Offline Name"), _("Fight Offline Kill Man"),),
        (_("Fight Online Score"), _("Fight Online Win Times"),),
    ]
    return val[rank_id][pos]


def ts2bantime(timestamp):
    if timestamp < time.time():
        return _('Not Time')
    return ts2time(timestamp)


register.filter(ts2date)
register.filter(ts2time)
register.filter(second2time)
register.filter(online)
register.filter(equiped)
register.filter(tab_join)
register.filter(filter_dungeon)
register.filter(filter_dungeon_label)
register.filter(enum_hero)
register.filter(enum_equip)
register.filter(enum_item)
register.filter(enum_restype)
register.filter(enum_building)
register.filter(rank_val)
register.filter(ts2bantime)
