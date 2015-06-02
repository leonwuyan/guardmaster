from detection.models import Excuse, Panel, UISubMenu, UIMainMenu, Tabel
from operating.models import Server
from guardmaster import common as Common
from operating.bbrr.api import ServerSocket
import logging
from pprint import pprint


class ServerControl(object):
    def __init__(self, server, uid, panel_id, username):
        super(ServerControl, self).__init__()
        self.server = server
        self.uid = uid
        self.panel_id = panel_id
        self.socketerror = {'result': -1}
        self.username = username

    def log(self, e):
        print __name__
        logger = logging.getLogger(__name__)
        d = {
            'username': self.username,
            'uid': self.uid,
            'server_name': self.server.label
        }
        s = "%(username)s|%(server_name)s|%(uid)s|" % d
        s = s + e
        logger.info(s)

    def _rank_list(self):
        if Common.E_RANKNAME_LIST is None:
            Common.E_RANKNAME_LIST = Tabel.get_enum(self.panel_id, Common.E_RANKNAME)
        return Common.E_RANKNAME_LIST

    def ranks(self):
        rank_list = self._rank_list()
        ranks = map(lambda x: {
                'label': x['EnumDes'],
                'id': x['EnumCd'],
            }, rank_list)
        return ranks

    def _params(self):
        ss = ServerSocket(self.server.ip, self.server.port)
        ret = ss.get_player_account(uid=self.uid)
        if ret['result'] != 0:
            return None, None, None, None
        uin = ret['uin']
        ret = ss.get_player_world_info(uin)
        world_info = ret['world_info']
        if len(world_info) == 0:
            return None, None, None, None
        world_info = Common.first(filter(lambda x: x['uid'] == self.uid, world_info))
        world_id = world_info['world_id']
        return ss, uin, world_id, world_info

    def base_info(self):
        (ss, uin, world_id, world_info) = self._params()
        if ss is None:
            return None
        ret = ss.get_player_base_info(self.uid, world_id)
        ret['uin'] = uin
        ret['world_id'] = world_id
        ret['world_info'] = world_info
        recharge = ss.get_player_total_recharge(self.uid, world_id)
        if recharge['result'] == 0:
            ret['total_recharge'] = recharge['total_recharge']
        building_info = ss.get_player_building_and_package(self.uid, world_id)
        if building_info['result'] != 0:
            return ret
        ret['building_data'] = building_info['building_info']['building_data']
        ret['package_data'] = building_info['building_info']['package_data']
        player_pve_info = ss.get_player_pve_info(self.uid, world_id)
        if player_pve_info['result'] != 0:
            return ret
        ret['pve_info'] = player_pve_info['pve_info']
        ret['hero_endless_info'] = player_pve_info['hero_endless_info']

        rank_list = self._rank_list()
        rank_list = map(lambda x: {
                'rank_name': x['EnumDes'],
                'rank_id': x['EnumCd'],
                'rank_info': ss.get_rank_pos(self.uid, world_id, x['EnumCd']),
            }, rank_list)
        ret['rank_list'] = rank_list
        return ret

    def send_mail(self, title, content):
        (ss, uin, world_id, world_info) = self._params()
        if ss is None:
            return None
        ret = ss.send_mail(
            [self.uid],
            world_id,
            {
                'mail_title': title,
                'mail_content': content,
                'mail_interval': 60*60*24*7,
            },
            []
        )
        return ret

    def add_attr(self, type_id, res_id=46, count=100000):
        (ss, uin, world_id, world_info) = self._params()
        if ss is None:
            return self.socketerror
        ret = ss.change_player_attr(self.uid, uin, world_id, type_id, res_id, count)
        return ret

    def add_vip_level(self, count=10000):
        (ss, uin, world_id, world_info) = self._params()
        if ss is None:
            return self.socketerror
        ret = ss.change_player_vip_level(self.uid, world_id, count)
        return ret

    def unlock_dungeon(self, dungeon_id):
        (ss, uin, world_id, world_info) = self._params()
        if ss is None:
            return self.socketerror
        ret = ss.change_player_unlock_dungeon(self.uid, uin, world_id, dungeon_id)
        return ret

    def kick(self):
        (ss, uin, world_id, world_info) = self._params()
        if ss is None:
            return self.socketerror
        ret = ss.kick_player(self.uid, uin, world_id)
        return ret

    def chat_ban(self, time):
        (ss, uin, world_id, world_info) = self._params()
        if ss is None:
            return self.socketerror
        ret = ss.ban_player_chat(self.uid, time, uin, world_id)
        return ret

    def account_ban(self, time):
        (ss, uin, world_id, world_info) = self._params()
        if ss is None:
            return self.socketerror
        ret = ss.lock_player(self.uid, time)
        return ret

    def all_rank(self, rank_id, rank_start, rank_count):
        ss = ServerSocket(self.server.ip, self.server.port)
        world_id = 1
        if rank_count <= 0:
            rank_count = 1
        rank = ss.get_rank_list(world_id, rank_id, rank_start, rank_count)
        for i in range(len(rank['rank_list'])):
            rank['rank_list'][i]['rank_pos'] = i+rank_start
        return rank
