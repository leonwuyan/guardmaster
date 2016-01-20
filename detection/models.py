from __future__ import absolute_import
from django.utils.translation import ugettext_lazy as _
from django.db import models, connections
from django.contrib.auth.models import Group
from django.shortcuts import get_object_or_404
from guardmaster import common as Common
from celery.task import task
import logging

# Create your models here.


class Excuse(models.Model):
    content = models.TextField()

    def __unicode__(self):
        return self.content

    class Meta:
        managed = False


class Panel(models.Model):
    label = models.CharField(max_length=45, unique=True)
    groups = models.ManyToManyField(Group)
    db_aliases = models.CharField(max_length=256)
    db_aliases_bak = models.CharField(max_length=256)
    start_date = models.DateField()
    symbol = models.CharField(max_length=45)

    def __unicode__(self):
        return self.label

    def get_id_label(self):
        ret = {
            'id': self.id,
            'label': self.label,
        }
        return ret


class UIMainMenu(models.Model):
    label = models.CharField(max_length=45)
    group = models.ManyToManyField(Group)
    panels = models.ManyToManyField(Panel)
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

    def is_in_panels(self, panel_id):
        panels = self.panels.all()
        for panel in panels:
            if panel.id == panel_id:
                return True
        return False

    class Meta:
        db_table = 'ui_main_menu'
        ordering = ['seqid']


class UISubMenu(models.Model):
    # CATEGORY_LIST is related with views(views.py)
    CATEGORY_LIST = {
        ('detection:count', _('count')),
        ('detection:count_with_pay_channel', _('count_with_pay_channel')),
        ('detection:count_without_time', _('count_without_time')),
        ('detection:count_only_time', _('count_only_time')),
        ('detection:user_query', _('user_query')),
        ('detection:gang_query', _('gang_query')),
        ('detection:deal_query', _('deal_query')),
        ('detection:history_query', _('history_query')),
        ('detection:ban_query', _('ban_query')),
        ('detection:bind_account', _('bind_account')),
        ('detection:everyday_history_query', _('everyday_history_query')),
        ('detection:everyday_deal_query', _('everyday_deal_query')),
        ('detection:chat_query', _('chat_query')),
        ('detection:online', _('online')),
        ('operating:notify', _('notify')),
        ('operating:mail', _('mail')),
        ('operating:all_mail', _('all_mail')),
        ('operating:single', _('single')),
        ('operating:rank', _('rank')),
        ('operating:contact', _('contact')),
        ('operating:guard_master_order', _('guard_master_order')),
        ('deployment:patch', _('patch')),
        ('deployment:config', _('config')),
        ('deployment:control', _('control')),
        ('deployment:pre_update', _('pre_update')),
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
    is_bak = models.BooleanField(default=False)
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
        ('pay_channel_list', _('pay channel list')),
        ('chat_type_list', _('chat type list')),
        ('user_status_list', _('user status list')),
        ('kick_ban', _('kick ban user')),
        ('ban_type', _('type of ban')),
        ('ban_time', _('time of ban')),
        ('contact_status', _('contact status')),
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


class Tabel(object):
    @classmethod
    def select_unsafe(self, sub_menu, panel, condition=None):
        if sub_menu.is_bak:
            db_name = panel.db_aliases_bak
        else:
            db_name = panel.db_aliases
        cursor = connections[db_name].cursor()
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
        return cursor.lastrowid

    @classmethod
    def update_unsafe(self, panel, condition):
        cursor = connections[panel.db_aliases].cursor()
        sql = "UPDATE %(table_name)s SET %(update)s WHERE %(condition)s" % condition
        logger = logging.getLogger(__name__)
        logger.info(sql)
        cursor.execute(sql)
        return cursor.fetchall()

    @classmethod
    def delete_unsafe(self, sub_menu, panel, condition=None):
        cursor = connections[panel.db_aliases].cursor()
        if condition:
            s = sub_menu.get_select_map()
            s['condition'] = condition
            sql = "DELETE FROM %(table_name)s WHERE %(condition)s" % s
        else:
            s = sub_menu.get_select_map()
            sql = "DELETE FROM %(table_name)s" % s
        logger = logging.getLogger(__name__)
        logger.info(sql)
        cursor.execute(sql)
        return cursor.lastrowid

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
    @task
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
    @task
    def update(self, panel, condition):
        if condition is None:
            return []
        try:
            ret = self.update_unsafe(panel, condition)
        except Exception as e:
            ret = []
            logger = logging.getLogger(__name__)
            logger.error(e)
        return ret

    @classmethod
    def delete(self, sub_menu, panel, condition=None):
        try:
            ret = self.delete_unsafe(sub_menu, panel, condition)
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
        ret = []
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
        ret = []
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
        tmp = ()
        if 'uin' in request_get:
            r = "Uin = '" + request_get.get('uin') + "'"
            tmp = tmp + (r,)
        if 'uid' in request_get:
            r = "UID = " + request_get.get('uid')
            tmp = tmp + (r,)
        if len(tmp) > 0:
            tmp = " OR ".join(tmp)
            condition = condition + (tmp,)
        if len(condition) > 0:
            condition = " AND ".join(condition)
        ret = self.select(sub_menu, panel, condition)
        return ret

    @classmethod
    def history_query_select(self, sub_menu, panel, request_get):
        condition = ()
        if 'start' in request_get:
            r = "CONCAT(LogDt,' ',LogTime)>='" + request_get.get('start') + "'"
            condition = condition + (r,)
        if 'end' in request_get:
            r = "CONCAT(LogDt,' ',LogTime)<'" + request_get.get('end') + "'"
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
    def ban_query_select(self, sub_menu, panel, request_get):
        condition = ()
        if 'uid' in request_get:
            r = "UID = " + request_get.get('uid')
            condition = condition + (r,)
        r = "(actType = 'account_ban' OR actType = 'chat_ban' OR actType = 'kick_ban')"
        condition = condition + (r,)
        if len(condition) > 0:
            condition = " AND ".join(condition)
            condition += " ORDER BY actDt DESC"
        ret = self.select(sub_menu, panel, condition)
        return ret

    @classmethod
    def chat_query_select(self, sub_menu, panel, request_get):
        condition = ()
        if 'start' in request_get:
            r = "LogDt>='" + request_get.get('start') + "'"
            condition = condition + (r,)
        if 'end' in request_get:
            r = "LogDt<'" + request_get.get('end') + "'"
            condition = condition + (r,)
        if 'chat_type' in request_get:
            r = "ChatType='" + request_get.get('chat_type') + "'"
            condition = condition + (r,)
        if 'user_status' in request_get:
            r = "BanStatus='" + request_get.get('user_status') + "'"
            condition = condition + (r,)
        if 'uid' in request_get:
            r = "UID = " + request_get.get('uid')
            condition = condition + (r,)
        if len(condition) > 0:
            condition = " AND ".join(condition)
            condition += " ORDER BY LogDt DESC"
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
        if 'uid' in request_get:
            r = "uid = '" + request_get.get('uid') + "'"
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
    def update_contact_status(self, panel, status, issue_id):
        condition = "issueid = " + str(issue_id)

        sqlset = "status = " + str(status)

        cond = {
            'table_name': 'tbClientIssue',
            'update': sqlset,
            'condition': condition,
        }
        ret = self.update(panel, cond)
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

    @classmethod
    def gm_log(self, panel_id, vals):
        panel = get_object_or_404(Panel, pk=panel_id)
        vals = "', '".join(vals)
        vals = "('" + vals + "')"
        condition = {
            'table_name': 'tbGMLog',
            'cols': "(`actDt`, `actDtSec`, `actUser`, `actIP`, `gmSrvIP`, `UID`, `ZoneID`, `ChannelID`, `actType`, `actObj`, `actRest`, `title`, `actStatus`, `doneDt`, `doneDtSec`)",
            'vals': vals,
        }
        ret = self.insert.delay(self, panel, condition)

    @classmethod
    def gm_res_log(self, panel_id, vals):
        panel = get_object_or_404(Panel, pk=panel_id)
        vals = "', '".join(vals)
        vals = "('" + vals + "')"
        condition = {
            'table_name': 'tbGMResLog',
            'cols': "(`actDt`, `actDtSec`, `actUser`, `actIP`, `gmSrvIP`, `UID`, `ZoneID`, `ChannelID`, `actType`, `emailID`, `chgType`, `chgValue`, `actStatus`, `doneDt`, `doneDtSec`)",
            'vals': vals,
        }
        ret = self.insert.delay(self, panel, condition)

    @classmethod
    def get_last_version(self, sub_menu, panel, request_get):
        condition = ()
        if 'hostname' in request_get:
            r = "hostname = '" + request_get['hostname'] + "'"
            condition = condition + (r,)
        if 'platform' in request_get:
            r = "platform = '" + request_get['platform'] + "'"
            condition = condition + (r,)
        if 'channel' in request_get:
            r = "channel = '" + request_get['channel'] + "'"
            condition = condition + (r,)
        if 'is_valid' in request_get:
            r = "is_valid = " + request_get['is_valid']
            condition = condition + (r,)
        if 'upt_typ' in request_get:
            r = "upt_typ = '" + request_get['upt_typ'] + "'"
            condition = condition + (r,)
        if len(condition) > 0:
            condition = " AND ".join(condition)
            condition += " ORDER BY client_id DESC LIMIT 1"
        ret = self.select(sub_menu, panel, condition)
        return ret

    @classmethod
    def update_tb_upt_conf(self, panel, update, request_get):
        condition = ()
        if 'hostname' in request_get:
            r = "hostname = '" + request_get['hostname'] + "'"
            condition = condition + (r,)
        if 'platform' in request_get:
            r = "platform = '" + request_get['platform'] + "'"
            condition = condition + (r,)
        if 'channel' in request_get:
            r = "channel = '" + request_get['channel'] + "'"
            condition = condition + (r,)
        if 'client_id' in request_get:
            r = "client_id = " + request_get['client_id']
            condition = condition + (r,)
        if 'update_id' in request_get:
            r = "update_id = " + request_get['update_id']
            condition = condition + (r,)
        if len(condition) >= 4:
            condition = " AND ".join(condition)
        else:
            return []
        sqlset = ()
        if 'is_valid' in update:
            r = "is_valid = " + update['is_valid']
            sqlset = sqlset + (r,)
        if len(sqlset) > 0:
            sqlset = ", ".join(sqlset)
        else:
            return []
        cond = {
            'table_name': 'tb_upt_conf',
            'update': sqlset,
            'condition': condition,
        }
        ret = self.update(panel, cond)
        return ret

    @classmethod
    def insert_tb_client_ver(self, panel, vals):
        vals = map(lambda x: str(x), vals)
        vals = "', '".join(vals)
        vals = "('" + vals + "')"
        condition = {
            'table_name': 'tb_client_ver',
            'cols': "(`ver_l1`, `ver_l2`, `ver_l3`, `ver_l4`, `is_valid`, `load_date`)",
            'vals': vals,
        }
        ret = self.insert(panel, condition)
        return ret

    @classmethod
    def insert_tb_upt_conf(self, panel, vals):
        vals = map(lambda x: str(x), vals)
        vals = "', '".join(vals)
        vals = "('" + vals + "')"
        condition = {
            'table_name': 'tb_upt_conf',
            'cols': "(`client_id`, `platform`, `hostname`, `channel`, `update_id`, `load_date`, `is_valid`)",
            'vals': vals,
        }
        ret = self.insert(panel, condition)
        return ret

    @classmethod
    def insert_tb_upt_info(self, panel, vals):
        vals = map(lambda x: str(x), vals)
        vals = "', '".join(vals)
        vals = "('" + vals + "')"
        condition = {
            'table_name': 'tb_upt_info',
            'cols': "(`upt_ver`, `upt_typ`, `file_name`, `addr`, `size`, `checksum`, `upt_date`, `load_date`)",
            'vals': vals,
        }
        ret = self.insert(panel, condition)
        return ret

    @classmethod
    def get_versions(self, sub_menu, panel, request_get):
        condition = ()
        if 'hostname' in request_get:
            r = "hostname = '" + request_get['hostname'] + "'"
            condition = condition + (r,)
        if 'platform' in request_get:
            r = "platform = '" + request_get['platform'] + "'"
            condition = condition + (r,)
        if 'channel' in request_get:
            r = "channel = '" + request_get['channel'] + "'"
            condition = condition + (r,)
        if 'is_valid' in request_get:
            r = "is_valid = " + request_get['is_valid']
            condition = condition + (r,)
        if 'upt_typ' in request_get:
            r = "upt_typ = '" + request_get['upt_typ'] + "'"
            condition = condition + (r,)
        if 'start' in request_get:
            r = "client_id > " + request_get['start']
            condition = condition + (r,)
        if 'end' in request_get:
            r = "client_id <= " + request_get['end']
            condition = condition + (r,)
        if len(condition) > 0:
            condition = " AND ".join(condition)
            condition += " ORDER BY client_id"
        ret = self.select(sub_menu, panel, condition)
        return ret

    @classmethod
    def pre_update_insert(self, panel, vals):
        vals = "', '".join(vals)
        vals = "('" + vals + "')"
        condition = {
            'table_name': 'tb_ip_channel',
            'cols': "(`ip`, `channel`)",
            'vals': vals,
        }
        ret = self.insert(panel, condition)
