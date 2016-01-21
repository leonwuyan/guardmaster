from deployment.models import *
from operating.models import Server
from django.utils import timezone
from django.shortcuts import get_object_or_404
from deployment.tasks import _sh
from celery.task import task
from time import time, localtime, strftime
import sys
import os


SCRIPT_SOURCE = '/var/lib/jenkins/workspace/bbrr_server_build/act_server/tools/servmgt/'
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPT_SH = os.path.join(BASE_DIR, 'script/')
SERVER_SCRIPT_DIR = '/mnt/smbci/servertools/update_tools/'
LIST_SCRIPT_DIR = '/mnt/smbci/servertools/update_tools/dolist/'
WORKING = 0
FAILED = 1
SUCCESSFUL = 2
LOCKING = 1
UNLOCK = 0


def _scp_script():
    IP = '192.168.1.76'
    PORT = '22'
    scp_cmd = "scp -P {0} root@{1}:{2}* {3}".format(
        PORT, IP, SCRIPT_SOURCE, SCRIPT_SH)
    retcode, output = _sh(BASE_DIR, scp_cmd)
    if retcode != 0:
        return False
    return True


def update_server_control_order(s, progress, result, status):
    s.progress = progress
    s.result = result
    s.status = status
    s.stop_date = timezone.now()
    s.save()


def is_server_control_order_locking(panel, server):
    try:
        sl = ServerControlWorkOrderLock.objects.filter(
            panel=panel, server=server.label)
        if sl:
            if len(sl) > 1:
                logger = logging.getLogger(__name__)
                error = '[Panel_ID:{1}]{0} Has More Than One Lock'.format(
                    server.label, panel.id)
                logger.error(error)
                return True
            sl = sl[0]
            if sl.status == LOCKING:
                return True
        else:
            sl = ServerControlWorkOrderLock(
                panel=panel,
                server=server.label,
                status=UNLOCK)
            sl.save()
    except Exception as e:
        print 'Exception :', e
        return True
    return False


def update_server_control_order_lock(panel, server, status):
    try:
        sl = ServerControlWorkOrderLock.objects.get(
            panel=panel, server=server.label)
        if sl:
            if sl.status == status:
                return False
            else:
                sl.status = status
                sl.save()
                print '[Panel_ID:{1}]{0} Status:{2}'.format(
                    server.label, panel.id, status)
                return True
    except Exception as e:
        logger = logging.getLogger(__name__)
        error = '[Panel_ID:{1}]{0} Has More Than One Lock'.format(
            server.label, panel.id)
        logger.error(error)
        return False
    return False


def _deployment(s, server):
    sco = get_object_or_404(ServerConfigOrder, pk=int(s.parameter1))
    server = get_object_or_404(Server, pk=int(s.parameter3))
    if s.parameter2 == 'A':
        cmd = "./create_delta_server_patch_file.sh {0} {1} {2} {3}".format(
            sco.ciwp,
            sco.version,
            sco.db_filename,
            sco.ps_filename)
    if s.parameter2 == 'B':
        cmd = "./push2pretest.sh {0} {1} {2} {3}".format(
            server.cdn_url,
            sco.ciwp,
            sco.version,
            sco.hs_filename)
    if s.parameter2 == 'C':
        cmd = "./push_version2server.sh {0} {1} {2} {3} {4}".format(
            server.cdn_url,
            sco.ciwp,
            sco.version,
            sco.hs_filename,
            server.perform)
    if s.parameter2 == 'D':
        cmd = "./push2pd.sh {0} {1} {2} {3} {4}".format(
            server.cdn_url,
            sco.ciwp,
            sco.version,
            sco.hs_filename,
            server.perform)
    if s.parameter2 == 'E':
        cmd = "./restore2pd.sh {0} {1} {2} {3} {4}".format(
            server.cdn_url,
            sco.ciwp,
            sco.version,
            sco.hs_filename,
            server.perform)
    retcode, output = _sh(SERVER_SCRIPT_DIR, cmd)
    if retcode != 0:
        return False
    return True


def _change_version(s, server):
    cmd = "sh -x ./chg_server_versions.sh {0} {1} {2} {3} {4}".format(
        server.ip, s.parameter1, s.parameter2, s.parameter3, s.parameter4)
    retcode, output = _sh(SCRIPT_SH, cmd)
    if retcode != 0:
        return False
    return True


@task
def deployment(fn, servercontrolworkorder_id, server_id):
    s = ServerControlWorkOrder.objects.get(pk=servercontrolworkorder_id)
    server = Server.objects.get(pk=server_id)
    if not _scp_script():
        update_server_control_order(s, s.progress, 'Error In Scp', FAILED)
        return
    if update_server_control_order_lock(s.panel, server, LOCKING):
        try:
            update_server_control_order(s, 20, 'Successful', SUCCESSFUL)
            func = globals()[fn]
            if func(s, server):
                update_server_control_order(s, 100, 'Successful', SUCCESSFUL)
            else:
                update_server_control_order(s, 0, 'Error In Srcipt', FAILED)
        except Exception as e:
            print 'Exception :', e
        finally:
            update_server_control_order_lock(
                s.panel, server, UNLOCK)


def server_control(fn, package):
    s = ServerControlWorkOrder(
        server=package['server'].label,
        panel=package['panel'],
        parameter1=package['parameter1'],
        parameter2=package['parameter2'],
        parameter3=package['parameter3'],
        parameter4=package['parameter4'],
        user=str(package['user']),
        progress=0,
        result='Working',
        status=WORKING,
        start_date=timezone.now(),
        stop_date=timezone.now())
    if is_server_control_order_locking(package['panel'], package['server']):
        update_server_control_order(s, 0, 'Order Is Locking', FAILED)
        return
    s.save()
    deployment.delay(fn, s.id, package['server'].id)


def _make_list_file(filename, tmp):
    filename = "{0}_{1}.list".format(
        filename, strftime('%Y%m%d%H%M%S', localtime(time())))
    file_path = LIST_SCRIPT_DIR + filename
    if len(tmp) > 0:
        tmp += '\n'
    try:
        with open(file_path, "w") as file:
            file.write(tmp)
        return filename
    except Exception as e:
        print e
    return 'NONE'


def make_list_file(sco, db, ps, hs, hs_free):
    mid_name = "{0}_{1}".format(sco.ciwp.label, sco.version)

    tmp = db
    db_filename = _make_list_file("{0}_{1}".format('databin', mid_name), tmp)
    sco.db_filename = db_filename
    sco.db_list = db

    if ps:
        ps_array = ps.split(',')
    else:
        ps_array = []
    content = []
    for i in ps_array:
        processserver = ProcessServer.objects.get(pk=int(i))
        content.append(processserver.label)
    tmp = "\n".join(content)
    ps_filename = _make_list_file("{0}_{1}".format('ps', mid_name), tmp)
    sco.ps_filename = ps_filename
    sco.ps_list = ps

    if hs:
        hs_array = hs.split(',')
    else:
        hs_array = []
    if hs_free:
        hs_free_array = hs_free.split(',')
    else:
        hs_free_array = []
    content = []
    for i in hs_array:
        processserver = ProcessServer.objects.get(pk=int(i))
        content.append("{0} 1".format(processserver.label))
    for i in hs_free_array:
        processserver = ProcessServer.objects.get(pk=int(i))
        content.append("{0} 2".format(processserver.label))
    tmp = "\n".join(content)
    hs_filename = _make_list_file("{0}_{1}".format('hotstart', mid_name), tmp)
    sco.hs_filename = hs_filename
    sco.hs_list = hs
    sco.hs_free_list = hs_free

    if hs_filename == 'NONE' or ps_filename == 'NONE' or hs_filename == 'NONE':
        sco.delete()
        return False
    else:
        sco.save()
        return True
