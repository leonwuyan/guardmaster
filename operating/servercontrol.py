from detection.models import Tabel
from operating.models import Server
from guardmaster import common as Common
from operating.bbrr.api import ServerSocket
from operating.models import ResponseMail
from django.utils import timezone
from pprint import pprint
import logging
import time


class ServerControl(object):
    def __init__(self, server, uid, panel_id, username, userip):
        super(ServerControl, self).__init__()
        self.server = server
        self.panel_id = panel_id
        self.socketerror = {'result': -1}
        self.success = {'result': 0}
        self.username = username
        self.userip = userip
        self.zone = 0
        self.channel = 0
        if uid.__class__.__name__ == 'int':
            self.uid = uid
            self.uids = [uid]
        else:
            self.uids = uid
            self.uid = uid[0]

    def log(self, e, uid=0):
        if uid == 0:
            uid = self.uid
        logger = logging.getLogger(__name__)
        d = {
            'username': self.username,
            'uid': uid,
            'server_name': self.server.label
        }
        s = "%(username)s|%(server_name)s|%(uid)s|" % d
        s = s + e
        logger.info(s)

    def db_log(self, obj, uid=0):
        Res = ['add', 'recharge', 'mail_acc']
        if 'type' not in obj:
            return False
        actDt = Common.now(obj['start_time'])
        actDtSec = int(obj['start_time'] * 1000 % 1000)
        doneDt = Common.now(obj['done_time'])
        doneDtSec = int(obj['done_time'] * 1000 % 1000)
        if uid == 0:
            uid = self.uid
        if obj['type'] in Res:
            vals = (
                actDt,
                str(actDtSec),
                self.username,
                self.userip,
                self.server.ip,
                str(uid),
                str(self.zone),
                str(self.channel),
                obj['type'],
                str(obj['post'].get('emailID')),
                str(obj['post'].get('type_id') or obj['post'].get('chgType')),
                str(obj['post'].get('count') or obj['post'].get('chgValue')),
                str(obj['ret']['result']),
                doneDt,
                str(doneDtSec))
            Tabel.gm_res_log(self.panel_id, vals)
        else:
            vals = (
                actDt,
                str(actDtSec),
                self.username,
                self.userip,
                self.server.ip,
                str(uid),
                str(self.zone),
                str(self.channel),
                obj['type'],
                str(obj['post'].get('actObj')),
                str(obj['post'].get('time') or
                    obj['post'].get('dungeon_id') or
                    obj['post'].get('actRest')),
                obj['post'].get('title', 'None'),
                str(obj['ret']['result']),
                doneDt,
                str(doneDtSec))
            Tabel.gm_log(self.panel_id, vals)
        return True

    def _rank_list(self):
        if Common.E_RANKNAME_LIST is None:
            Common.E_RANKNAME_LIST = Tabel.get_enum(self.panel_id, Common.E_RANKNAME)
        return Common.E_RANKNAME_LIST

    def ranks(self):
        rank_list = self._rank_list()
        ranks = map(lambda x: {
                'label': x['EnumDes'],
                'id': int(x['EnumCd']),
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
        self.zone = world_id
        self.channel = world_info['channel_id']
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
                'rank_id': int(x['EnumCd']),
                'rank_info': ss.get_rank_pos(self.uid, world_id, int(x['EnumCd'])),
            }, rank_list)
        ret['rank_list'] = rank_list
        return ret

    def _send_mail(self, title, content, acc=[]):
        (ss, uin, world_id, world_info) = self._params()
        if ss is None:
            return None
        start_time = time.time()
        ret = ss.send_mail(
            self.uids,
            world_id,
            {
                'mail_title': title,
                'mail_content': content,
                'mail_interval': 60*60*24*7,
            },
            acc
        )
        return ret

    def send_mail(self, title=None, content=None, post=None):
        start_time = time.time()
        if post is None:
            ret = self._send_mail(title, content)
            response_id = Common.first(ret['sucess_result'])['mail_id']
            self.db_log({
                'type': 'contact',
                'post': {
                    'title': title,
                    'actRest': response_id},
                'ret': ret,
                'start_time': start_time,
                'done_time': time.time(),
            })
            return ret
        title = post.get('title', 'Title')
        content = post.get('content', 'Content')
        acc = []
        if post.get('crystal', None):
            crystal = int(post.get('crystal'))
            acc.append({'res_type': 1, 'res_id': 0, 'res_count': crystal})
        if post.get('gold', None):
            gold = int(post.get('gold'))
            acc.append({'res_type': 2, 'res_id': 0, 'res_count': gold})
        if post.get('money', None):
            money = int(post.get('money'))
            acc.append({'res_type': 3, 'res_id': 0, 'res_count': money})
        if post.get('skillpoint', None):
            skillpoint = int(post.get('skillpoint'))
            acc.append({'res_type': 4, 'res_id': 0, 'res_count': skillpoint})
        if post.get('power', None):
            power = int(post.get('power'))
            acc.append({'res_type': 6, 'res_id': 0, 'res_count': power})
        if post.get('score', None):
            score = int(post.get('score'))
            acc.append({'res_type': 11, 'res_id': 0, 'res_count': score})
        if len(post.getlist('acc', [])) > 0:
            for k in post.getlist('acc'):
                if len(acc) < 6:
                    t = k.split("|")
                    (a, b, c) = (int(t[0]), int(t[1]), int(t[2]))
                    acc.append({'res_type': a, 'res_id': b, 'res_count': c})
        ret = self._send_mail(title, content, acc)
        for p in ret['sucess_result']:
            if ret['result'] == self.success['result']:
                r = ResponseMail(
                        title=title,
                        content=content,
                        server=self.server,
                        guardmaster=self.username,
                        uid=p['uid'],
                        accessory=str(acc),
                        response_id=p['mail_id'],
                        pub_date=timezone.now()
                    )
                r.save()
                s = 'mail|' + str(r.id)
                self.log(s, p['uid'])
            if len(acc) > 0:
                for a in acc:
                    self.db_log({
                        'type': 'mail_acc',
                        'post': {
                            'emailID': p['mail_id'],
                            'chgType': a['res_type'],
                            'chgValue': a['res_count']},
                        'ret': ret,
                        'start_time': start_time,
                        'done_time': time.time(),
                    }, p['uid'])
            else:
                self.db_log({
                    'type': 'mail',
                    'post': {
                        'title': title,
                        'actObj': r.id,
                        'actRest': p['mail_id']},
                    'ret': ret,
                    'start_time': start_time,
                    'done_time': time.time(),
                }, p['uid'])
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

    def all_rank(self, world_id, rank_id, rank_start, rank_count):
        ss = ServerSocket(self.server.ip, self.server.port)
        if rank_count <= 0:
            rank_count = 1
        rank = ss.get_rank_list(world_id, rank_id, rank_start, rank_count)
        for i in range(len(rank['rank_list'])):
            rank['rank_list'][i]['rank_pos'] = i+rank_start
        return rank
