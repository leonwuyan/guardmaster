from operating.models import Notify, CDNServer
from django.shortcuts import get_object_or_404
from detection.models import Panel
import subprocess
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
        list_cdn = panel.cdnserver_set.all()
        for cdn in list_cdn:
            cmd = 'scp -P ' + str(cdn.port) + ' -r ' + BASE_DIR + OPERATING_DIR
            cmd += ' ' + cdn.ip + ':' + cdn.home
            ret = subprocess.Popen(cmd, shell=True)
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
            return post.get(k)
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