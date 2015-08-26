from __future__ import absolute_import
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
    logger = logging.getLogger(__name__)
    for k in output:
        logger.info(k)


def _sh(path, cmd):
    spend_time = time.time()
    cmd = ' '.join(cmd)
    s = subprocess.Popen(cmd, shell=True, cwd=path, stdout=subprocess.PIPE)
    retcode = s.wait()
    output = s.communicate()
    spend_time = str(time.time() - spend_time)
    logger = logging.getLogger(__name__)
    logger.info(path + '|' + cmd + '|' + str(retcode) + '|' + spend_time)
    print_output(output)


@task
def _do_sh(*cmds):
    logger = logging.getLogger(__name__)
    logger.info('CMDS START')
    for cmd in cmds:
        _sh(cmd[0], cmd[1:])
    logger.info('CMDS END')
