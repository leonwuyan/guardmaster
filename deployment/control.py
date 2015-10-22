from deployment.models import ServerControlWorkOrderLock, ServerControlWorkOrder
from operating.models import Server
from django.utils import timezone
from deployment.tasks import _sh
from celery.task import task
import sys
import os


SCRIPT_SOURCE = '/var/lib/jenkins/workspace/bbrr_server_build/act_server/tools/servmgt/'
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPT_SH = os.path.join(BASE_DIR, 'script/')
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
    cmd = "sh -x ./auto_deploy_tools_adv.sh stage={1} release={2} version={4} servip={0} CIWP={3}".format(
        server.ip, s.parameter1, s.parameter2, s.parameter3, s.parameter4)
    retcode, output = _sh(SCRIPT_SH, cmd)
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
    deployment(fn, s.id, package['server'].id)