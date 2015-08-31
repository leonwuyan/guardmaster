from __future__ import absolute_import
from deployment.models import UpLoadWorkOrder, HostName
from deployment.version import Version
from operating.models import Server
from detection.models import Panel
from django.utils import timezone
from celery.task import task
import subprocess
import logging
import time


@task
def _do_kground_work(name):
    for i in range(1, 10):
        print 'hello:%s %s' % (name, i)
        time.sleep(1)


def print_output(output):
    if output.__class__ is tuple:
        for k in output:
            print k


def _sh(path, cmd):
    spend_time = time.time()
    cmd = ' '.join(cmd)
    s = subprocess.Popen(cmd, shell=True, cwd=path, stdout=subprocess.PIPE)
    retcode = s.wait()
    output = s.communicate()
    spend_time = str(time.time() - spend_time)
    logger = logging.getLogger(__name__)
    loginfo = '{0}|{1}|{2}|{3}'.format(path, cmd, str(retcode), spend_time)
    logger.info(loginfo)
    print loginfo
    print_output(output)


@task
def _do_sh(*cmds):
    print '---------- CMDS START ----------'
    for cmd in cmds:
        _sh(cmd[0], cmd[1:])
    print '---------- CMDS END ----------'


@task
def _upload_patch(uploadworkorder_id, server_id, dir_path):
    u = UpLoadWorkOrder.objects.get(pk=uploadworkorder_id)
    s = Server.objects.get(pk=server_id)
    print u
    print s
    print dir_path
    while u.progress < 100:
        u.progress += 10
        u.save()
        time.sleep(1)


def upload_patch(panel, server, hostname, platform, channel, version, user):
    u = UpLoadWorkOrder(
        server=server.label,
        panel=panel,
        hostname=hostname.label,
        platform=platform,
        channel=channel,
        version=str(version),
        user=str(user),
        progress=0,
        result='Working',
        start_date=timezone.now(),
        stop_date=timezone.now())
    u.save()
    _upload_patch.delay(u.id, server.id, hostname.dir_path)
