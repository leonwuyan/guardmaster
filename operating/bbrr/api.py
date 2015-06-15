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
    def __init__(self, ip, port):
        super(ServerSocket, self).__init__()
        self.pkg_head_length = 32
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
        if p == 'int' or p == 'unicode' or p == 'bool':
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
        st = struct.Struct('16sIIII' + str(len(data)) + 's')

        pkg_data = st.pack(*pkg)
        un_pkg_data = st.unpack(pkg_data)

        return pkg_data

    def parse_pkg_body(self, data):
        st = struct.Struct(str(len(data)) + 's')
        body = st.unpack(data)

        return body

    def parse_pkg_head(self, data):
        st = struct.Struct('16sIIII')
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
        s.settimeout(5.0)
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
            )
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
            return self.success
        return {'result': 1, 'failed_uid': self.res(pb.failed_uid)}

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
