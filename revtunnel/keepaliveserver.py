import os
import time
import stat
import glob
import subprocess

SSH_PATH = '/home/imehedi/.ssh/'
TOUCH_F = SSH_PATH + 'paramiko.exists'
# Get test file stats
stats = os.stat(TOUCH_F)
mod_time = stats[stat.ST_MTIME]
cur_time = time.time()
# See if more than 6 mins have passed since test file was modified
if cur_time - mod_time > 360:
    files = glob.glob('/home/imehedi/.ssh/revssh_*')
    for fl in files:
        path, pid = fl.split('_')
    pid.strip()
    try:
        os.kill(int(pid), 9)
    except OSError:
        pass
    os.unlink(fl)

    ssh_proc = subprocess.Popen(['ssh', '-N', 'XXX.XXX.XXX.XXX', '&'])
    fname = SSH_PATH + 'revssh_' + str(ssh_proc.pid)
    fh = open(fname, 'w')
