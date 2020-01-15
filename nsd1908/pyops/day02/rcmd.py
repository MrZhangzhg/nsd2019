import paramiko
import sys
import getpass
import os
import threading

def rcmd(host, user, passwd, command):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, username=user, password=passwd)
    stdin, stdout, stderr = ssh.exec_command(command)
    out = stdout.read()
    err = stderr.read()
    if out:  # 如果out非空
        print('\033[32;1m[%s] OUT\033[0m:\n%s' % (host, out.decode()))
    if err:
        print('\033[31;1m[%s] ERROR\033[0m:\n%s' % (host, err.decode()))
    ssh.close()

if __name__ == '__main__':
    # rcmd('192.168.4.4', 'root', '123456', 'id root; id zhangsan')
    if len(sys.argv) != 3:
        print("Usage: %s ipfile 'commands'" % sys.argv[0])
        exit(1)
    if not os.path.isfile(sys.argv[1]):
        print('No such file:', sys.argv[1])
        exit(2)

    ipfile = sys.argv[1]
    cmds = sys.argv[2]
    passwd = getpass.getpass()
    with open(ipfile) as fobj:
        for line in fobj:
            ip = line.strip()
            # rcmd(ip, 'root', passwd, cmds)
            t = threading.Thread(target=rcmd, args=(ip, 'root', passwd, cmds))
            t.start()
