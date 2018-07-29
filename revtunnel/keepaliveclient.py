import paramiko
import os
import glob
import subprocess

IP = 'XXX.XXX.XXX.XXX'

SSH_PATH = '/home/imehedi/.ssh/'
HOST_KEYS = SSH_PATH + 'paramiko.hosts'


def keepaliveclient():
    client = paramiko.SSHClient()

    client.load_host_keys(HOST_KEYS)
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(IP, port=9999, username='imehedi',timeout=30)
        stdin, stdout, stderr = client.exec_command('touch ~/.ssh/paramiko.exists')
        client.save_host_keys(HOST_KEYS)
    except Exception, e:
        print e
    files = glob.glob('/home/imehedi/.ssh/revssh_*')

    for fl in files:
        path, pid = fl.split('_')
        pid.strip()
        try:
            os.kill(int(pid), 9)
        except OSError:
        pass
        os.unlink(fl)

    ssh_proc = subprocess.Popen(['ssh', '-N', 'localhost', '&'])
    fname = SSH_PATH + 'revssh_' + str(ssh_proc.pid)
    fh = open(fname, 'w')


if __name__ == '__main__':
    keepaliveclient()
