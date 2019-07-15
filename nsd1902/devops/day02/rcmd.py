#!/root/nsd1902/bin/python
import paramiko
import sys
import getpass
import threading
import os

def rcmd(host, user='root', passwd=None, port=22, command=None):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, username=user, password=passwd, port=port)
    stdin, stdout, stderr = ssh.exec_command(command)
    out = stdout.read()
    err = stderr.read()
    if out:
        print('[\033[34;1m%s\033[0m] \033[32;1mOUT\033[0m:\n%s' % (host, out.decode()))
    if err:
        print('[\033[34;1m%s\033[0m] \033[31;1mERROR\033[0m:\n%s' % (host, err.decode()))
    ssh.close()

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: %s ipfile "command"' % sys.argv[0])
        exit(1)

    if not os.path.isfile(sys.argv[1]):
        print('No such file: %s' % sys.argv[1])
        exit(2)

    ipfile = sys.argv[1]
    command = sys.argv[2]
    passwd = getpass.getpass()
    with open(ipfile) as fobj:
        for line in fobj:
            ip = line.strip()  # 去除行尾的\n，得到IP地址
            t = threading.Thread(target=rcmd, args=(ip,), kwargs={'passwd': passwd, 'command': command})
            t.start()  # rcmd(*args, **kwargs)
            # rcmd(ip, passwd=passwd, command=command)
