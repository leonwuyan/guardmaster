from operating.models import Notify
from django.shortcuts import get_object_or_404
from guardmaster import common as Common
from detection.models import Panel
import subprocess
import logging
import json
import os


class NotifyDeployment(object):
    def __init__(self, panel_id, username):
        super(NotifyDeployment, self).__init__()
        self.panel_id = panel_id
        self.username = username
        self.cdn_url = []

    def _tiitle(self, t, is_title):
        before = "<stroke size=2 color='0x0000417'><gradient direction=y start_color='0xFFFFFF' end_color='0xFFB300'>"
        after = "</gradient></stroke>"
        if is_title:
            return before + t + after
        else:
            return ""

    def _channel_plus(self, channel):
        channel_plus = {
            '20015': ['20016'],
            '20025': ['20035'],
            '20026': ['20036'],
            '20028': ['20038'],
        }
        for k in channel_plus.keys():
            if k in channel:
                for i in channel_plus[k]:
                    channel.append(i)
        return channel

    def _n(self, n):
        channel = n.channel.split(',')
        world_id = n.world_id.split(',')
        platform = n.platform.split(',')
        channel = self._channel_plus(channel)
        for i in channel:
            for j in world_id:
                for k in platform:
                    path = '/'.join([n.hostname, str(i), k, str(j)])
                    if self.json.get(path, None) is None:
                        self.json[path] = []
                    self.json[path].append({
                        'Name': str(n.id),
                        'Title': self._tiitle(n.title, n.is_title),
                        'Link': n.link,
                        'ImageWidth': n.image_width,
                        'ImageHeight': n.image_height,
                        'Start': Common.datetime2ts(n.start, 28800),
                        'End': Common.datetime2ts(n.end, 28800),
                        'Content': n.content,
                        'Version': n.version,
                        'IsDisplay': n.is_display,
                    })

    def _json(self):
        for k in self.json.keys():
            ret = {'msg': self.json[k]}
            ret = json.dumps(ret, ensure_ascii=False)
            self.json[k] = ret

    def _writejson(self):
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        OPERATING_DIR = '/operating/notify/'
        self.cdn_url = []
        panel = get_object_or_404(Panel, pk=self.panel_id)
        servers = panel.server_set.all()
        for server in servers:
            path = BASE_DIR + OPERATING_DIR + server.hostname + '/'
            if os.path.exists(path):
                cmd = 'rm -rf *'
                s = subprocess.Popen(cmd, shell=True, cwd=path, stdout=subprocess.PIPE)
                retcode = s.wait()
                logger = logging.getLogger(__name__)
                logger.info(self.username + '|' + path + '|' + cmd + '|' + str(retcode))
        for k in self.json.keys():
            path = BASE_DIR + OPERATING_DIR + k
            if not os.path.exists(path):
                os.makedirs(path)
            file_path = path + '/n.json'
            self.cdn_url.append(k + '/n.json')
            with open(file_path, "w") as file:
                file.write(self.json[k].encode('utf-8'))

    def _scpjson(self, panel):
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        OPERATING_DIR = '/operating/notify/'
        list_cdn = panel.server_set.filter(server_type='cdn')
        logger = logging.getLogger(__name__)
        for cdn in list_cdn:
            cmd = 'rsync -e "ssh -p ' + str(cdn.ssh_port) + '" -zr --delete '
            cmd += BASE_DIR + OPERATING_DIR
            cmd += ' ' + cdn.ip + ':' + cdn.home
            ret = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
            logger.info(self.username + '|' + cmd)
        self.cdn_url = map(lambda x: cdn.cdn_url + 'notify/' + x, self.cdn_url)

    def tojson(self):
        panel = get_object_or_404(Panel, pk=self.panel_id)
        list_notify = panel.notify_set.all()
        self.json = {}
        map(lambda x: self._n(x), list_notify)
        self._json()
        self._writejson()
        self._scpjson(panel)
        return self.cdn_url

    def _get(self, post, k):
        if post.get(k):
            return post.get(k).replace('"', "'").replace('#', '').replace('&nbsp;', ' ').replace('&lt;br&gt;', '<br>')
        return None

    def add(self, post):
        panel = get_object_or_404(Panel, pk=self.panel_id)
        channel = ','.join(post.getlist('channel'))
        platform = ','.join(post.getlist('platform'))
        zone = ','.join(post.getlist('zone'))
        if post.get('is_title'):
            is_title = True
        else:
            is_title = False
        if 'id' in post:
            n = get_object_or_404(Notify, pk=post.get('id'))
            n.title = self._get(post, 'title')
            n.content = self._get(post, 'content')
            n.is_display = post.get('is_display')
            n.link = post.get('link')
            n.image_width = post.get('width')
            n.image_height = post.get('height')
            n.hostname = post.get('hostname')
            n.channel = channel
            n.version = post.get('version')
            n.is_title = is_title
            n.platform = platform
            n.world_id = zone
            n.start = post.get('start')
            n.end = post.get('end')
            n.seqid = self._get(post, 'seqid')
        else:
            n = Notify(
                title=self._get(post, 'title'),
                content=self._get(post, 'content'),
                panel=panel,
                is_display=post.get('is_display'),
                link=post.get('link'),
                image_width=post.get('width'),
                image_height=post.get('height'),
                hostname=post.get('hostname'),
                channel=channel,
                version=post.get('version'),
                is_title=is_title,
                platform=platform,
                world_id=zone,
                start=post.get('start'),
                end=post.get('end'),
                seqid=self._get(post, 'seqid')
            )
        ret = 1
        try:
            n.save()
        except Exception as e:
            ret = 2
        return ret
