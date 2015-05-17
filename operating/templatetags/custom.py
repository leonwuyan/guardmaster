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
        return None
    return datetime.datetime.fromtimestamp(ts)


def ts2time(timestamp):
    try:
        ts = int(timestamp)
    except ValueError:
        return None
    return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(ts))


def second2time(second):
    try:
        ss = int(second)
    except ValueError:
        return None
    t = {
        'hour': ss / 3600,
        'minute': (ss % 3600) / 60,
        'second': ss % 60,
    }
    return _("%(hour)s H %(minute)s M %(second)s S") % t


def online(is_online):
    if is_online == 0:
        return _("OFF LINE")
    else:
        return _("ON LINE")


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


register.filter(ts2date)
register.filter(ts2time)
register.filter(second2time)
register.filter(online)
register.filter(equiped)
register.filter(tab_join)
register.filter(filter_dungeon)
register.filter(filter_dungeon_label)
