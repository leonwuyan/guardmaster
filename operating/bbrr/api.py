#!/usr/bin/python
# coding:utf-8

import socket
import google.protobuf
import proto.guard_proto_pb2
import proto.proto_factory
from proto.string_hash import StringHash
from notification import XgNotification
import sys
import ctypes
import struct
import binascii
import xinge
from pprint import pprint

# content = u'推送测试,全部设备'
# title = u'安卓抬头'
# x = XgNotification(XgNotification.ANDROID)
# tag_list = ('1', '2')
# print x.query_tag_token_num('1')
# msg = x.build_msg(content, title)
# print x.push_all_devices(msg)


class ServerSocket(object):
    def __init__(self, ip, port, buf):
        super(ServerSocket, self).__init__()
        self.pkg_buf = buf
        self.pkg_head_length = 32 + buf
        self.ip = ip
        self.port = port
        self.empty = {'result': 3}
        self.timeout = {'result': 2}
        self.success = {'result': 0}

    def _getattr(self, pb, attr):
        if pb.__class__ is dict:
            return pb[attr]
        return getattr(pb, attr)

    def pb2dict(self, pb, attrs):
        ret = {}
        for attr in attrs:
            ret[attr] = self.res(self._getattr(pb, attr))
        return ret

    def res(self, pb):
        p = pb.__class__.__name__
        if p == 'int' or p == 'unicode' or p == 'bool' or p == 'long':
            return pb
        if p == 'RepeatedCompositeFieldContainer':
            return map(lambda x: self.res(x), pb)
        if p == 'RepeatedScalarFieldContainer':
            return map(lambda x: self.res(x), pb)
        ret = proto.proto_factory.res(self.pb2dict, pb)
        if ret is None:
            print 'p :', p
        return ret

    def serialize_pkg(self, phash, data):
        length = socket.htonl(len(data))
        uid = socket.htonl(1)
        type_h = socket.htonl(phash)
        seq_no = socket.htonl(0)
        pkg = ('DD', length, uid, type_h, seq_no, data)
        l = str(16 + self.pkg_buf)
        st = struct.Struct(l + 'sIIII' + str(len(data)) + 's')

        pkg_data = st.pack(*pkg)
        un_pkg_data = st.unpack(pkg_data)

        return pkg_data

    def parse_pkg_body(self, data):
        st = struct.Struct(str(len(data)) + 's')
        body = st.unpack(data)

        return body

    def parse_pkg_head(self, data):
        l = str(16 + self.pkg_buf)
        st = struct.Struct(l + 'sIIII')
        head = st.unpack(data)
        head_safe = (
            head[0],
            socket.ntohl(head[1]),
            socket.ntohl(head[2]),
            socket.ntohl(head[3]),
            socket.ntohl(head[4]))

        return head_safe

    def create_pb(self, pstr, data):
        phash = StringHash.calculate_hash(pstr)
        pb = proto.proto_factory.create_pb(phash)
        for key in data:
            if data[key].__class__.__name__ == 'list':
                for i in data[key]:
                    tlist = getattr(pb, key)
                    tlist.append(i)
            else:
                setattr(pb, key, data[key])

        return phash, pb

    def serialize_pb(self, pstr, data):
        (phash, pb) = self.create_pb(pstr, data)

        return phash, pb.SerializeToString()

    def parse_pb(self, phash, pbdata):
        pstr = proto.proto_factory.get_pb_name(phash)
        pb = proto.proto_factory.create_pb(phash)
        pb.ParseFromString(pbdata)

        return pstr, pb

    def recv_pkg(self, s, size):
        l = 0
        ret = ''
        try:
            while l < size:
                data = s.recv(size)
                l += len(data)
                ret += data
        except socket.timeout as e:
            ret = None
        return ret

    def connect_server(self, ip, port, content):
        address = (ip, port)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(30.0)
        try:
            s.connect(address)
        except Exception, e:
            return {'result': -1}
        ret = s.send(content)
        data = self.recv_pkg(s, self.pkg_head_length)
        if data is None:
            return {'result': 2}
        if not data.strip():
            return {'result': 3}
        un_pkg_head = self.parse_pkg_head(data)
        data = self.recv_pkg(s, un_pkg_head[1])
        un_pkg_body = self.parse_pkg_body(data)
        (pstr, pb) = self.parse_pb(un_pkg_head[3], un_pkg_body[0])
        s.close()
        return pb

    def send_server_mail(self, uids, world_id, mail_info, mail_accs):
        mail = {'world_id': world_id}
        (phash_mail, pb_mail) = self.create_pb('GM_SEND_MAIL_REQ', mail)
        for uid in uids:
            pb_mail.uid.append(uid)
        pb_mail_info = pb_mail.mail_info
        pb_mail_info.mail_title = mail_info['mail_title']
        pb_mail_info.mail_content = mail_info['mail_content']
        pb_mail_info.mail_interval = mail_info['mail_interval']
        for mail_acc in mail_accs:
            pb_mail_info.mail_acc.add(
                res_type=mail_acc['res_type'],
                res_id=mail_acc['res_id'],
                res_count=mail_acc['res_count'],
                res_extern_param_1=mail_acc.get('res_extern_param_1', 0),
                res_extern_param_2=mail_acc.get('res_extern_param_2', 0),
                res_extern_param_3=mail_acc.get('res_extern_param_3', 0),
            )
        pkggg = self.serialize_pkg(phash_mail, pb_mail.SerializeToString())
        return self.connect_server(self.ip, self.port, pkggg)

    def send_gameserver_mail(self, world_id, mail_info, mail_accs, condition, online):
        mail = {'world_id': world_id, 'is_send_online': online}
        (phash_mail, pb_mail) = self.create_pb('GM_SEND_GAMESERVER_MAIL_REQ', mail)
        pb_mail_info = pb_mail.mail_info
        pb_mail_info.mail_title = mail_info['mail_title']
        pb_mail_info.mail_content = mail_info['mail_content']
        pb_mail_info.mail_interval = mail_info['mail_interval']
        for mail_acc in mail_accs:
            pb_mail_info.mail_acc.add(
                res_type=mail_acc['res_type'],
                res_id=mail_acc['res_id'],
                res_count=mail_acc['res_count'],
                res_extern_param_1=mail_acc.get('res_extern_param_1', 0),
                res_extern_param_2=mail_acc.get('res_extern_param_2', 0),
                res_extern_param_3=mail_acc.get('res_extern_param_3', 0),
            )
        pb_mail_condition = pb_mail.mail_condition
        pb_mail_condition.effect_begin_time = condition['begin']
        pb_mail_condition.effect_end_time = condition['end']
        pb_mail_condition.effect_clt_version = condition['version']
        pb_mail_condition.effect_channel_id = condition['channel']
        pb_mail_condition.effect_player_state = condition['status']
        pkggg = self.serialize_pkg(phash_mail, pb_mail.SerializeToString())
        return self.connect_server(self.ip, self.port, pkggg)

    def send_server(self, proto, req):
        (phash, pb) = self.serialize_pb(proto, req)
        pkggg = self.serialize_pkg(phash, pb)
        return self.connect_server(self.ip, self.port, pkggg)

    def _get(self, p, r):
        pb = self.send_server(p, r)
        if self._getattr(pb, 'result') == 0:
            return self.res(pb)
        return {'result': self._getattr(pb, 'result')}

    def get_player_account(self, uid=None, name=None):
        if uid is None and name is None:
            return self.empty
        if uid is not None:
            p = 'GM_GET_PLAYER_ACCOUNT_BY_UID_REQ'
            r = {'uid': uid, }
        if name is not None:
            p = 'GM_GET_PLAYER_ACCOUNT_BY_NAME_REQ'
            r = {'role_name': name, }
        return self._get(p, r)

    def get_player_world_info(self, uin):
        if uin is None:
            return self.empty
        p = 'GM_GET_PLAYER_WORLD_INFO_REQ'
        r = {'uin': uin}
        return self._get(p, r)

    def get_player_base_info(self, uid, world_id):
        if uid is None or world_id is None:
            return self.empty
        p = 'GM_GET_PLAYER_BASE_INFO_REQ'
        r = {'uid': uid, 'world_id': world_id}
        return self._get(p, r)

    def get_rank_list(self, world_id, rank_id, start_pos, get_count):
        if start_pos is None or rank_id is None or world_id is None or get_count is None:
            return self.empty
        p = 'GM_GET_RANK_LIST_REQ'
        r = {
            'world_id': world_id,
            'rank_id': rank_id,
            'start_pos': start_pos,
            'get_count': get_count,
        }
        return self._get(p, r)

    def get_rank_pos(self, uid, world_id, rank_id):
        if uid is None or rank_id is None or world_id is None:
            return self.empty
        p = 'GM_GET_RANK_POS_BY_UID_REQ'
        r = {'uid': uid, 'world_id': world_id, 'rank_id': rank_id}
        return self._get(p, r)

    def get_player_pve_info(self, uid, world_id):
        if uid is None or world_id is None:
            return self.empty
        p = 'GM_GET_PLAYER_PVE_INFO_REQ'
        r = {'uid': uid, 'world_id': world_id}
        return self._get(p, r)

    def get_player_building_and_package(self, uid, world_id):
        if uid is None or world_id is None:
            return self.empty
        p = 'GM_GET_PLAYER_BUILDING_AND_PACKAGE_REQ'
        r = {'uid': uid, 'world_id': world_id}
        return self._get(p, r)

    def get_player_total_recharge(self, uid, world_id):
        if uid is None or world_id is None:
            return self.empty
        p = 'GM_GET_PLAYER_TOTAL_RECHARGE_REQ'
        r = {'uid': uid, 'world_id': world_id}
        return self._get(p, r)

    def lock_player(self, uid, lock_time):
        if uid is None or lock_time is None:
            return self.empty
        p = 'GM_LOCK_PLAYER_REQ'
        r = {'uid': uid, 'lock_time': lock_time}
        return self._get(p, r)

    def ban_player_chat(self, uid, ban_time, uin, world_id):
        if uid is None or ban_time is None or uin is None or world_id is None:
            return self.empty
        p = 'GM_BAN_PLAYER_CHAT_REQ'
        r = {'uid': uid, 'ban_time': ban_time, 'uin': uin, 'world_id': world_id}
        return self._get(p, r)

    def kick_player(self, uid, uin, world_id):
        if uid is None or world_id is None or uin is None:
            return self.empty
        p = 'GM_KICK_PLAYER_REQ'
        r = {'uid': uid, 'world_id': world_id, 'uin': uin}
        return self._get(p, r)

    def send_mail(self, uids, world_id, mail_info, mail_accs):
        if uids is None or world_id is None or mail_info is None or mail_accs is None:
            return self.empty
        if len(uids) > 1000:
            return self.empty
        pb = self.send_server_mail(uids, world_id, mail_info, mail_accs)
        if pb.__class__ is dict:
            return self.timeout
        if len(pb.failed_uid) == 0:
            ret = self.success
            ret['sucess_result'] = self.res(pb.sucess_result)
            return ret
        return {'result': 1, 'failed_uid': self.res(pb.failed_uid)}

    def send_all_mail(self, world_id, mail_info, mail_accs, condition, online):
        if world_id is None or mail_info is None or mail_accs is None:
            return self.empty
        if condition is None or online is None:
            return self.empty
        pb = self.send_gameserver_mail(world_id, mail_info, mail_accs, condition, online)
        if pb.__class__ is dict:
            return self.timeout
        return self.res(pb)

    def get_all_mail(self, world_id):
        if world_id is None:
            return self.empty
        p = 'GM_GET_GAMESERVER_MAIL_INFO_REQ'
        r = {'world_id': world_id}
        return self._get(p, r)

    def del_all_mail(self, world_id, mail_seq_key):
        if world_id is None or mail_seq_key is None:
            return self.empty
        p = 'GM_DEL_GAMESERVER_MAIL_REQ'
        r = {'world_id': world_id, 'mail_seq_key': mail_seq_key}
        return self._get(p, r)

    def change_player_attr(self, uid, uin, world_id, res_type, res_id, chg_count):
        if uid is None or world_id is None or uin is None:
            return self.empty
        if res_type is None or res_id is None or chg_count is None:
            return self.empty
        p = 'GM_CHG_PLAYER_ATTR_REQ'
        r = {
            'uid': uid, 'world_id': world_id, 'uin': uin,
            'res_type': res_type, 'res_id': res_id, 'chg_count': chg_count,
        }
        return self._get(p, r)

    def change_player_hero_level(self, uid, uin, world_id, hero_id, hero_lv, hero_exp):
        if uid is None or world_id is None or uin is None:
            return self.empty
        if hero_id is None or hero_lv is None or hero_exp is None:
            return self.empty
        p = 'GM_CHG_PLAYER_HERO_LEVEL_REQ'
        r = {
            'uid': uid, 'world_id': world_id, 'uin': uin,
            'hero_id': hero_id, 'hero_lv': hero_lv, 'hero_exp': hero_exp,
        }
        return self._get(p, r)

    def change_player_vip_level(self, uid, world_id, total_recharge):
        if uid is None or world_id is None or total_recharge is None:
            return self.empty
        p = 'GM_CHG_PLAYER_VIP_LEVEL_REQ'
        r = {
            'uid': uid, 'world_id': world_id, 'total_recharge': total_recharge,
        }
        return self._get(p, r)

    def change_player_unlock_dungeon(self, uid, uin, world_id, unlock_til_dungeon_id):
        if uid is None or world_id is None or uin is None:
            return self.empty
        if unlock_til_dungeon_id is None:
            return self.empty
        p = 'GM_CHG_PLAYER_UNLOCK_DUNGEON_REQ'
        r = {
            'uid': uid, 'world_id': world_id, 'uin': uin,
            'unlock_til_dungeon_id': unlock_til_dungeon_id,
        }
        return self._get(p, r)

    def get_player_first_purchase(self, world_id, uid, channel):
        if world_id is None or uid is None or channel is None:
            return self.empty
        p = 'GM_GET_PLAYER_FIRST_PURCHASE'
        r = {'world_id': world_id, 'uid': uid, 'channel': channel}
        return self._get(p, r)

    def del_player_equiped_equip(self, uid, world_id, uin, hero_id, equip_id):
        if world_id is None or uid is None or uin is None or hero_id is None or equip_id is None:
            return self.empty
        p = 'GM_DEL_PLAYER_EQUIPED_EQUIP_REQ'
        r = {
            'world_id': world_id,
            'uid': uid,
            'uin': uin,
            'hero_id': hero_id,
            'equip_id': equip_id
            }
        return self._get(p, r)

    def del_player_from_gang(self, uid, world_id):
        if world_id is None or uid is None:
            return self.empty
        p = 'GM_DEL_PLAYER_FROM_GANG_REQ'
        r = {'world_id': world_id, 'role_id': uid}
        return self._get(p, r)

    def del_player_from_rank(self, uid, world_id, rank_id):
        if world_id is None or uid is None or rank_id is None:
            return self.empty
        p = 'GM_DEL_PLAYER_FROM_RANK_REQ'
        r = {'world_id': world_id, 'role_id': uid, 'rank_id': rank_id}
        return self._get(p, r)

    def get_player_month_card(self, uid, world_id):
        if world_id is None or uid is None:
            return self.empty
        p = 'GM_GET_PLAYER_MONTH_CARD_REQ'
        r = {'world_id': world_id, 'uid': uid}
        return self._get(p, r)

    def change_player_month_card(self, uid, world_id, change_days, card_id=1):
        if world_id is None or uid is None:
            return self.empty
        p = 'GM_CHG_PLAYER_MONTH_CARD_REQ'
        r = {
            'world_id': world_id,
            'uid': uid,
            'card_id': card_id,
            'change_days': change_days
        }
        return self._get(p, r)

    def guard_copy_gm_text(self, gm_text, param, uid, uin, world_id):
        if world_id is None or uid is None or gm_text is None or param is None:
            return self.empty
        if uin is None:
            return self.empty
        p = 'GUARD_COPY_GM_TEXT_REQ'
        r = {
            'world_id': world_id,
            'uid': uid,
            'gm_text': gm_text,
            'param': param,
            'uin': uin}
        return self._get(p, r)

    def get_gang_base_info(self, gang_id, world_id):
        if world_id is None or gang_id is None:
            return self.empty
        p = 'GM_GET_GANG_BASE_INFO_REQ'
        r = {'world_id': world_id, 'gang_id': gang_id}
        return self._get(p, r)

    def modify_gang_base_info(self, gang_id, world_id, gang_base_info):
        if world_id is None or gang_id is None or gang_base_info is None:
            return self.empty
        p = 'GM_MODIFY_GANG_BASE_INFO_REQ'
        r = {'world_id': world_id, 'gang_id': gang_id}
        (phash_gang, pb_gang) = self.create_pb(p, r)
        if gang_base_info.get('gang_score'):
            pb_gang.gang_base_info.gang_score = gang_base_info.get('gang_score')
        if gang_base_info.get('gang_notify'):
            pb_gang.gang_base_info.gang_notify = gang_base_info.get('gang_notify')
        pkggg = self.serialize_pkg(phash_gang, pb_gang.SerializeToString())
        pb = self.connect_server(self.ip, self.port, pkggg)
        if pb.__class__ is dict:
            return self.timeout
        return self.res(pb)

    def modify_dun_data(self, uid, world_id, is_del, dun_data_info):
        if world_id is None or uid is None or is_del is None:
            return self.empty
        if dun_data_info is None:
            return self.empty
        p = 'GM_MODIFY_DUN_DATA_REQ'
        r = {'world_id': world_id, 'uid': uid, 'is_del': is_del}
        (phash_dun, pb_dun) = self.create_pb(p, r)
        for dun_data in dun_data_info:
            pb_dun.dun_info.add(
                dun_id=dun_data.get('dun_id'),
                dun_star=dun_data.get('dun_star'))
        pkggg = self.serialize_pkg(phash_dun, pb_dun.SerializeToString())
        pb = self.connect_server(self.ip, self.port, pkggg)
        if pb.__class__ is dict:
            return self.timeout
        return self.res(pb)
