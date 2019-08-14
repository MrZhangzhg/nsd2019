import paramiko
import threading
import sys
import os
import getpass

def rcmd(host, user='root', passwd=None, port=22, cmds=None):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=host, port=port, username=user, password=passwd)
    stdin, stdout, stderr = ssh.exec_command(cmds)
    out = stdout.read()
    err = stderr.read()
    if out:
        print('[%s] \033[32;1mOUT\033[0m:\n%s' % (host, out.decode()))
    if err:
        print('[%s] \033[31;1mERROR\033[0m:\n%s' % (host, err.decode()))
    ssh.close()

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: %s ipfile "commands"' % sys.argv[0])
        exit(1)

    if not os.path.isfile(sys.argv[1]):
        print('No such file %s' % sys.argv[1])
        exit(2)

    hostfile = sys.argv[1]
    cmds = sys.argv[2]
    password = getpass.getpass()
    with open(hostfile) as fobj:
        for line in fobj:
            ip = line.strip()
            # rcmd(ip, passwd=password, cmds=cmds)
            t = threading.Thread(target=rcmd, args=(ip,), kwargs={'passwd': password, 'cmds': cmds})
            t.start()  # target(*args, **kwargs)
