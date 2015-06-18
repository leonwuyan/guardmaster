from django.utils.translation import ugettext_lazy as _
from django.db import models, connections
from django.contrib.auth.models import Group
from django.shortcuts import get_object_or_404
from guardmaster import common as Common
import logging

# Create your models here.


class Excuse(models.Model):
    content = models.TextField()

    def __unicode__(self):
        return self.content

    class Meta:
        managed = False


class UIMainMenu(models.Model):
    label = models.CharField(max_length=45)
    groups = models.ManyToManyField(Group)
    seqid = models.IntegerField()

    def __unicode__(self):
        return self.label

    def get_sub_menu_keys(self, sub_menu, keys):
        return map(lambda k: getattr(sub_menu, k), keys)

    def get_sub_menu_dict(self, keys):
        cols = self.uisubmenu_set.all()
        vals = map(lambda x: self.get_sub_menu_keys(x, keys), cols)
        return Common.kvs(keys, vals)

    def get_sub_menu_all(self):
        ret = {
            'label': self.label,
            'sub_menu': self.get_sub_menu_dict(['label', 'url', 'category'])
        }
        return ret

    class Meta:
        db_table = 'ui_main_menu'
        ordering = ['seqid']


class UISubMenu(models.Model):
    # CATEGORY_LIST is related with views(views.py)
    CATEGORY_LIST = {
        ('detection:count', _('count')),
        ('detection:count_without_time', _('count_without_time')),
        ('detection:count_only_time', _('count_only_time')),
        ('detection:user_query', _('user_query')),
        ('detection:gang_query', _('gang_query')),
        ('detection:deal_query', _('deal_query')),
        ('detection:history_query', _('history_query')),
        ('operating:notify', _('notify')),
        ('operating:mail', _('mail')),
        ('operating:single', _('single')),
        ('operating:rank', _('rank')),
        ('operating:contact', _('contact')),
    }
    label = models.CharField(max_length=45)
    main_menu = models.ForeignKey(UIMainMenu, blank=True, null=True)
    url = models.CharField(max_length=200, db_index=True)
    table_name = models.CharField(max_length=45, blank=True, null=True)
    category = models.CharField(
        max_length=45,
        blank=True,
        null=True,
        help_text=_('Category is required when Main menu is selected'),
        choices=CATEGORY_LIST)
    seqid = models.IntegerField()

    def __unicode__(self):
        return self.label

    def get_col_map_vals(self, val):
        cols = self.uicolmap_set.all()
        return map(lambda x: getattr(x, val), cols)

    def get_select_map(self):
        select_map = {
            'cols': ','.join(self.get_col_map_vals('col_name')),
            'table_name': self.table_name
        }
        return select_map

    def get_col_map_keys(self, col_map, keys):
        return map(lambda k: getattr(col_map, k), keys)

    def get_col_map_dict(self, keys):
        cols = self.uicolmap_set.all()
        vals = map(lambda x: self.get_col_map_keys(x, keys), cols)
        return Common.kvs(keys, vals)

    class Meta:
        db_table = 'ui_sub_menu'
        ordering = ['main_menu', 'seqid']


class UIColMap(models.Model):
    # COL_TYPE_LIST is related with ValueFormat(value_format.py)
    COL_TYPE_LIST = {
        ('date', _('date')),
        ('time', _('time')),
        ('timestamp_to_date', _('timestamp to date')),
        ('timestamp_to_time', _('timestamp to time')),
        ('float_two', _('float two')),
        ('ratio_two', _('ratio two')),
        ('channel_list', _('channel list')),
        ('zone_list', _('zone list')),
        ('identity_str', _('anything to string')),
        ('contact_reply', _('contact to reply')),
        ('ip_to_server', _('ip to server')),
    }
    label = models.CharField(max_length=45)
    sub_menu = models.ForeignKey(UISubMenu)
    col_name = models.CharField(max_length=45)
    col_type = models.CharField(
        max_length=45,
        blank=True, null=True,
        choices=COL_TYPE_LIST)
    seqid = models.IntegerField()

    def __unicode__(self):
        return self.label

    class Meta:
        db_table = 'ui_col_map'
        ordering = ['sub_menu', 'seqid']


class Panel(models.Model):
    label = models.CharField(max_length=45, unique=True)
    groups = models.ManyToManyField(Group)
    db_aliases = models.CharField(max_length=45)
    symbol = models.CharField(max_length=45)

    def __unicode__(self):
        return self.label

    def get_id_label(self):
        ret = {
            'id': self.id,
            'label': self.label,
        }
        return ret


class Tabel(object):
    @classmethod
    def select_unsafe(self, sub_menu, panel, condition=None):
        cursor = connections[panel.db_aliases].cursor()
        if condition:
            s = sub_menu.get_select_map()
            s['condition'] = condition
            sql = "SELECT %(cols)s FROM %(table_name)s WHERE %(condition)s" % s
        else:
            s = sub_menu.get_select_map()
            sql = "SELECT %(cols)s FROM %(table_name)s" % s
        logger = logging.getLogger(__name__)
        logger.info(sql)
        cursor.execute(sql)
        return cursor.fetchall()

    @classmethod
    def insert_unsafe(self, panel, condition):
        cursor = connections[panel.db_aliases].cursor()
        sql = "INSERT INTO %(table_name)s %(cols)s VALUES %(vals)s" % condition
        logger = logging.getLogger(__name__)
        logger.info(sql)
        cursor.execute(sql)
        return cursor.fetchall()

    @classmethod
    def select(self, sub_menu, panel, condition=None):
        try:
            ret = self.select_unsafe(sub_menu, panel, condition)
        except Exception as e:
            ret = []
            logger = logging.getLogger(__name__)
            logger.error(e)
        return ret

    @classmethod
    def insert(self, panel, condition):
        if condition is None:
            return []
        try:
            ret = self.insert_unsafe(panel, condition)
        except Exception as e:
            ret = []
            logger = logging.getLogger(__name__)
            logger.error(e)
        return ret

    @classmethod
    def count_select(self, sub_menu, panel, request_get):
        condition = ()
        if 'start' in request_get:
            r = "StDate >= '" + request_get.get('start') + "'"
            condition = condition + (r,)
        if 'end' in request_get:
            r = "StDate <= '" + request_get.get('end') + " 24:00:00'"
            condition = condition + (r,)
        if 'zone_id[]' in request_get:
            r = ",".join(request_get.getlist('zone_id[]'))
            r = "ZoneID IN (" + r + ")"
            condition = condition + (r,)
        if 'channel_id[]' in request_get:
            r = ",".join(request_get.getlist('channel_id[]'))
            r = "ChannelID IN (" + r + ")"
            condition = condition + (r,)
        if len(condition) > 0:
            condition = " AND ".join(condition)
        ret = self.select(sub_menu, panel, condition)
        return ret

    @classmethod
    def count_only_time_select(self, sub_menu, panel, request_get):
        condition = ()
        if 'start' in request_get:
            r = "StDate >= '" + request_get.get('start') + "'"
            condition = condition + (r,)
        if 'end' in request_get:
            r = "StDate <= '" + request_get.get('end') + " 24:00:00'"
            condition = condition + (r,)
        if len(condition) > 0:
            condition = " AND ".join(condition)
        ret = self.select(sub_menu, panel, condition)
        return ret

    @classmethod
    def count_without_time_select(self, sub_menu, panel, request_get):
        condition = ()
        if 'zone_id[]' in request_get:
            r = ",".join(request_get.getlist('zone_id[]'))
            r = "ZoneID IN (" + r + ")"
            condition = condition + (r,)
        if 'channel_id[]' in request_get:
            r = ",".join(request_get.getlist('channel_id[]'))
            r = "ChannelID IN (" + r + ")"
            condition = condition + (r,)
        if len(condition) > 0:
            condition = " AND ".join(condition)
        ret = self.select(sub_menu, panel, condition)
        return ret

    @classmethod
    def user_qeury_select(self, sub_menu, panel, request_get):
        condition = ()
        if 'uin' in request_get:
            r = "Uin = '" + request_get.get('uin') + "'"
            condition = condition + (r,)
        if 'name' in request_get:
            r = "Name like '%" + request_get.get('name') + "%'"
            condition = condition + (r,)
        if 'uid' in request_get:
            r = "UID = " + request_get.get('uid')
            condition = condition + (r,)
        if len(condition) > 0:
            condition = " OR ".join(condition)
        ret = self.select(sub_menu, panel, condition)
        return ret

    @classmethod
    def gang_qeury_select(self, sub_menu, panel, request_get):
        condition = ()
        if 'g_n' in request_get:
            r = "GangName like '%" + request_get.get('g_n') + "%'"
            condition = condition + (r,)
        if 'g_l_n' in request_get:
            r = "GangLeaderName like '%" + request_get.get('g_l_n') + "%'"
            condition = condition + (r,)
        if 'g_i' in request_get:
            r = "GangID = " + request_get.get('g_i')
            condition = condition + (r,)
        if len(condition) > 0:
            condition = " OR ".join(condition)
        ret = self.select(sub_menu, panel, condition)
        return ret

    @classmethod
    def deal_query_select(self, sub_menu, panel, request_get):
        condition = ()
        if 'start' in request_get:
            r = "StDate >= '" + request_get.get('start') + "'"
            condition = condition + (r,)
        if 'end' in request_get:
            r = "StDate <= '" + request_get.get('end') + "'"
            condition = condition + (r,)
        if 'moneys' in request_get:
            r = "money >= " + request_get.get('moneys')
            condition = condition + (r,)
        if 'moneye' in request_get:
            r = "money <= " + request_get.get('moneye')
            condition = condition + (r,)
        if len(condition) > 0:
            condition = (" AND ".join(condition), )
        if 'uin' in request_get:
            r = "Uin = '" + request_get.get('uin') + "'"
            condition = condition + (r,)
        if 'uid' in request_get:
            r = "UID = " + request_get.get('uid')
            condition = condition + (r,)
        if len(condition) > 0:
            condition = " OR ".join(condition)
        ret = self.select(sub_menu, panel, condition)
        return ret

    @classmethod
    def history_query_select(self, sub_menu, panel, request_get):
        print request_get
        condition = ()
        if 'start' in request_get:
            r = "LogDt >= '" + request_get.get('start') + "'"
            condition = condition + (r,)
        if 'end' in request_get:
            r = "LogDt <= '" + request_get.get('end') + "'"
            condition = condition + (r,)
        if 'server' in request_get:
            r = "Server = '" + request_get.get('server') + "'"
            condition = condition + (r,)
        if 'uid' in request_get:
            r = "UID = " + request_get.get('uid')
            condition = condition + (r,)
        if len(condition) > 0:
            condition = " AND ".join(condition)
            condition += " ORDER BY Server, UID, LogDt, LogTime, EventTyp"
        ret = self.select(sub_menu, panel, condition)
        return ret

    @classmethod
    def contact_select(self, sub_menu, panel, request_get):
        condition = ()
        if 'start' in request_get:
            r = "opentime >= '" + request_get.get('start') + "'"
            condition = condition + (r,)
        if 'end' in request_get:
            r = "opentime <= '" + request_get.get('end') + " 24:00:00'"
            condition = condition + (r,)
        if 'hostname' in request_get:
            r = "hostname = '" + request_get.get('hostname') + "'"
            condition = condition + (r,)
        if len(condition) > 0:
            condition = " AND ".join(condition)
        if 'id' in request_get:
            condition = "issueid = " + request_get.get('id')
        ret = self.select(sub_menu, panel, condition)
        return ret

    @classmethod
    def contact_insert(self, panel, vals):
        vals = "', '".join(vals)
        vals = "('" + vals + "')"
        condition = {
            'table_name': 'tbClientResponse',
            'cols': "(`issueid`, `title`, `content`, `updatetime`, `updateoper`, `emailID`)",
            'vals': vals,
        }
        ret = self.insert(panel, condition)

    @classmethod
    def contact_reply_select(self, panel, issue_id):
        sub_menu = get_object_or_404(UISubMenu, url=Common.CONTACT_REPLY)
        keys = sub_menu.get_col_map_vals('col_name')
        condition = "issueid = " + issue_id
        ret = self.select(sub_menu, panel, condition)
        ret = Common.kvs(keys, ret)
        return ret

    @classmethod
    def get_enum(self, panel_id, enum_en):
        panel = get_object_or_404(Panel, pk=panel_id)
        enum_submenu = get_object_or_404(UISubMenu, url=Common.ENUM)
        keys = enum_submenu.get_col_map_vals('col_name')
        condition = "EnumEn = '" + enum_en + "'"
        enum = Tabel.select(enum_submenu, panel, condition)
        ret_enum = Common.kvs(keys, enum)
        return ret_enum
