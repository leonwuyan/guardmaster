from operating.models import Notify
from django.shortcuts import get_object_or_404
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

    def _n(self, n):
        path = '/'.join([
            n.hostname,
            str(n.channel),
            n.platform,
            str(n.world_id)
        ])
        if self.json.get(path, None) is None:
            self.json[path] = []
        self.json[path].append({
            'Name': str(n.id),
            'Title': n.title,
            'Link': n.link,
            'Content': n.content,
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
                logger.info(path + '|' + cmd + '|' + str(retcode))
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
            cmd = 'scp -P ' + str(cdn.ssh_port) + ' -r '
            cmd += BASE_DIR + OPERATING_DIR
            cmd += ' ' + cdn.ip + ':' + cdn.home
            ret = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
            logger.info(cmd)
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
        notify_url = '/'.join([
            post.get('hostname'),
            post.get('channel'),
            post.get('platform'),
            post.get('zone'),
            'n.json'
        ])
        if 'id' in post:
            n = get_object_or_404(Notify, pk=post.get('id'))
            n.title = self._get(post, 'title')
            n.content = self._get(post, 'content')
            n.is_display = post.get('is_display')
            n.link = post.get('link')
            n.hostname = post.get('hostname')
            n.channel = post.get('channel')
            n.platform = post.get('platform')
            n.world_id = post.get('zone')
            n.notify_url = notify_url
            n.seqid = self._get(post, 'seqid')
        else:
            n = Notify(
                title=self._get(post, 'title'),
                content=self._get(post, 'content'),
                panel=panel,
                is_display=post.get('is_display'),
                link=post.get('link'),
                hostname=post.get('hostname'),
                channel=post.get('channel'),
                platform=post.get('platform'),
                world_id=post.get('zone'),
                notify_url=notify_url,
                seqid=self._get(post, 'seqid')
            )
        ret = 1
        try:
            n.save()
        except Exception as e:
            ret = 2
        return ret
