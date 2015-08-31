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
import sys
import os

local_path_Mac = '/Volumes/91ACT_CONTROL/clientupdate/'
local_path_CentOS = '/mnt/smbcontrol/clientupdate/'


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
    if cmd.__class__.__name__ != 'str':
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
    return retcode, output


@task
def _do_sh(*cmds):
    print '---------- CMDS START ----------'
    for cmd in cmds:
        _sh(cmd[0], cmd[1:])
    print '---------- CMDS END ----------'


def _scp_single_zip(ip, local_path, remote_path, file_name):
    local_file = local_path + file_name
    scp_cmd = "scp {0} root@{1}:{2}".format(local_file, ip, remote_path)
    retcode, output = _sh(BASE_DIR, scp_cmd)
    if retcode != 0:
        return False

    local_size = os.path.getsize(local_path)
    tools_path = "{0}tools/".format(local_path_CentOS)
    checksum_cmd = "./checksum {0}".format(local_path)
    retcode, output = _sh(tools_path, checksum_cmd)
    print 'checksum :', output
    return True


def scp_path(u, server, local_path, remote_path):
    file_list = os.listdir(local_path)
    progress_total = len(file_list)
    if progress_total == 0:
        u.result = 'Not Any Files'
        u.save()
        return False

    mkdir_cmd = "ssh root@{0} 'mkdir -p {1}'".format(server.ip, remote_path)
    retcode, output = _sh(BASE_DIR, mkdir_cmd)

    progress = 0
    for f in file_list:
        if _scp_single_zip(server.ip, local_path, remote_path, f):
            progress += 1
            u.progress = progress * 100 / progress_total
            u.save()
        else:
            u.result = 'Error In Scp'
            u.save()
            return False
    u.result = 'Successful'
    u.save()
    return True


@task
def _upload_patch(uploadworkorder_id, server_id, dir_path):
    u = UpLoadWorkOrder.objects.get(pk=uploadworkorder_id)
    s = Server.objects.get(pk=server_id)
    app_path = '.'.join(u.version.split('.')[:3])
    version_path = u.version.split('.')[3:][0]
    local_path = '{0}{1}/{2}/{3}/{4}/{5}/'.format(
        local_path_CentOS,
        dir_path,
        u.channel,
        app_path,
        version_path,
        u.platform
    )
    print local_path
    if not os.path.exists(local_path):
        u.result = 'Dir Do Not Exists'
        u.save()
        return
    remote_path = '{0}{1}/{2}/{3}/{4}/{5}/'.format(
        s.home,
        dir_path,
        u.channel,
        app_path,
        version_path,
        u.platform
    )
    print remote_path
    if scp_path(u, s, local_path, remote_path):
        pass


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
