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
        ('detection:user_query', _('user_query')),
        ('detection:gang_query', _('gang_query')),
        ('detection:deal_query', _('deal_query')),
    }
    label = models.CharField(max_length=45)
    main_menu = models.ForeignKey(UIMainMenu, blank=True, null=True)
    url = models.CharField(max_length=200, db_index=True, unique=True)
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
        print 'SQL :', sql
        cursor.execute(sql)
        return cursor.fetchall()

    @classmethod
    def select(self, sub_menu, panel, condition=None):
        try:
            ret = self.select_unsafe(sub_menu, panel, condition)
        except Exception as e:
            ret = []
            print 'Exception :', e
        return ret

    @classmethod
    def count_select(self, sub_menu, panel, request_get):
        condition = ()
        if 'start' in request_get:
            r = "StDate >= '" + request_get.get('start') + "'"
            condition = condition + (r,)
        if 'end' in request_get:
            r = "StDate <= '" + request_get.get('end') + "'"
            condition = condition + (r,)
        if 'zone_id[]' in request_get:
            r = ",".join(request_get.getlist('zone_id[]'))
            r = "ZoneID IN (" + r + ")"
            condition = condition + (r,)
        if 'channel_id[]' in request_get:
            r = ",".join(request_get.getlist('channel_id[]'))
            r = "ChannelID IN (" + r + ")"
            condition = condition + (r,)
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
        condition = (" AND ".join(condition), )
        if 'uin' in request_get:
            r = "Uin = '" + request_get.get('uin') + "'"
            condition = condition + (r,)
        if 'uid' in request_get:
            r = "UID = " + request_get.get('uid')
            condition = condition + (r,)
        condition = " OR ".join(condition)
        ret = self.select(sub_menu, panel, condition)
        return ret

    @classmethod
    def get_list(self, panel, url):
        ret_list = get_object_or_404(UISubMenu, url=url)
        ret_keys = ret_list.get_col_map_vals('col_name')
        ret_list = Tabel.select(ret_list, panel)
        ret_list = Common.kvs(ret_keys, ret_list)
        return ret_list