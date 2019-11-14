import paramiko
import sys
import getpass
import threading
import os

def rcmd(host, user='root', passwd=None, port=22, cmd=None):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, username=user, port=port, password=passwd)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    out = stdout.read()
    err = stderr.read()
    if out:  # 如果有输出
        print('[\033[32;1m%s\033[0m] OUT:\n%s' % (host, out.decode()))
    if err:
        print('[\033[31;1m%s\033[0m] ERROR:\n%s' % (host, err.decode()))
    ssh.close()

if __name__ == '__main__':
    # rcmd('192.168.1.10', passwd='123456', cmd='id root; id zhangsan')
    if len(sys.argv) != 3:
        print("Usage: %s ipfile 'command'" % sys.argv[0])
        exit(1)

    if not os.path.isfile(sys.argv[1]):
        print('No such file:', sys.argv[1])
        exit(2)

    ipfile = sys.argv[1]
    cmd = sys.argv[2]
    passwd = getpass.getpass()
    with open(ipfile) as fobj:
        for line in fobj:
            ip = line.strip()  # 去除行尾的\n
            # rcmd(ip, passwd=passwd, cmd=cmd)
            t = threading.Thread(
                target=rcmd, args=(ip,),
                kwargs={'passwd': passwd, 'cmd': cmd}
            )
            t.start()  # rcmd(*args, **kwargs)
