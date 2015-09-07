from __future__ import absolute_import
from deployment.models import UpLoadWorkOrder, HostName
from django.shortcuts import render, get_object_or_404
from guardmaster import common as Common
from deployment.version import Version
from operating.models import Server
from detection.models import Panel, Tabel, UISubMenu
from django.utils import timezone
from celery.task import task
import subprocess
import logging
import time
import sys
import os

local_path_Mac = '/Volumes/91ACT_CONTROL/clientupdate/'
local_path_CentOS = '/mnt/smbcontrol/clientupdate/'
SH_PATH = local_path_CentOS
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


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
    return True


def _info_single_zip(addr_path, file_name):
    local_file = SH_PATH + addr_path + file_name
    local_path = SH_PATH + addr_path
    local_size = os.path.getsize(local_file)
    tools_path = "{0}tools/".format(SH_PATH)
    checksum_cmd = "./checksum {0}{1}".format(local_path, file_name)
    retcode, output = _sh(tools_path, checksum_cmd)
    checksum = output[0]
    return local_size, checksum


def get_client_id(panel, version):
    sub_menu = get_object_or_404(UISubMenu, url=Common.CLIENT_ID)
    condition = "concat(ver_l1,'.',ver_l2,'.' ,ver_l3,'.' ,ver_l4)='{0}'".format(version)
    ret = Tabel.select(sub_menu, panel, condition)
    try:
        ret = ret[0][0]
    except Exception as e:
        ret = 0
    return ret


def insert_client_id(panel, version):
    v = version.split('.')
    client_id = Tabel.insert_tb_client_ver(panel, [
        v[0], v[1], v[2], v[3], '1', timezone.now()])
    return client_id


def insert_upt(u, server, client_id, file_name, addr_path, app_url=None):
    TYP = u.platform
    v = u.version.split('.')
    if v[3] == '0':
        TYP += '_app'
        addr = app_url
        local_size = checksum = '0'
        file_name = 'None'
    else:
        TYP += '_patch'
        addr = addr_path + file_name
        local_size, checksum = _info_single_zip(addr_path, file_name)
    update_id = Tabel.insert_tb_upt_info(u.panel, [
        v[3], TYP, file_name, addr, local_size, checksum,
        timezone.now(), timezone.now()])
    ret = Tabel.insert_tb_upt_conf(u.panel, [
        client_id, u.platform, u.hostname, u.channel,
        update_id, timezone.now(), '0'])
    return update_id


def clean_up_tb(u, server):
    client_id = get_client_id(u.panel, u.version)
    if client_id == 0:
        client_id = insert_client_id(u.panel, u.version)
    else:
        update = {'is_valid': '0'}
        request_get = {
            'hostname': u.hostname,
            'platform': u.platform,
            'channel': str(u.channel),
            'client_id': str(client_id),
        }
        Tabel.update_tb_upt_conf(u.panel, update, request_get)
    return client_id


def _update_bbc_list(u, server, local_path, addr_path):
    client_id = clean_up_tb(u, server)
    file_list = os.listdir(local_path)
    file_list = filter(lambda x: x.find('.zip') > 0, file_list)
    update_list = []
    for f in file_list:
        update_id = insert_upt(u, server, client_id, f, addr_path)
        update_list.append({
            'client_id': client_id,
            'hostname': u.hostname,
            'platform': u.platform,
            'channel': u.channel,
            'update_id': update_id,
            })
    return update_list


def scp_patch(u, server, local_path, remote_path):
    file_list = os.listdir(local_path)
    file_list = filter(lambda x: x.find('.zip') > 0, file_list)
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
    return True


@task
def _upload_patch(uploadworkorder_id, server_id, addr_path):
    u = UpLoadWorkOrder.objects.get(pk=uploadworkorder_id)
    s = Server.objects.get(pk=server_id)
    local_path = SH_PATH + addr_path
    if not os.path.exists(local_path):
        u.result = 'Dir Do Not Exists'
        u.save()
        return
    remote_path = s.home + addr_path
    if scp_patch(u, s, local_path, remote_path):
        update_list = _update_bbc_list(u, server, local_path, addr_path)
        u.result = 'Successful'
        u.save()
        print 'UPDATE_LIST :', update_list


@task
def _upload_app(uploadworkorder_id, server_id, app_url):
    u = UpLoadWorkOrder.objects.get(pk=uploadworkorder_id)
    s = Server.objects.get(pk=server_id)
    client_id = clean_up_tb(u, s)
    udpate_id = insert_upt(u, s, client_id, None, None, app_url)


def upload_version(
        panel, server, hostname, platform,
        channel, version, user, app_url):
    if True:
        pass
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
    app_path = '.'.join(u.version.split('.')[:3])
    version_path = u.version.split('.')[3:][0]
    addr_path = '{0}/{1}/{2}/{3}/{4}/'.format(
        hostname.dir_path,
        u.channel,
        app_path,
        version_path,
        u.platform)
    if version.is_app():
        _upload_app.delay(u.id, server.id, app_url)
    else:
        _upload_patch.delay(u.id, server.id, addr_path)
