import getpass
import paramiko
import threading
import sys
import os

def rcmd(host, user='root', passwd=None, port=22, commands=None):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, username=user, password=passwd, port=port)
    stdin, stdout, stderr = ssh.exec_command(commands)

    out = stdout.read()
    err = stderr.read()
    if out:
        print('[\033[32;1m%s\033[0m] OUT:\n%s' % (host, out.decode()))
    if err:
        print('[\033[31;1m%s\033[0m] ERROR:\n%s' % (host, err.decode()))

    ssh.close()

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: %s ipfile "commands"' % sys.argv[0])
        exit(1)

    # 地址文件必须存在
    if not os.path.isfile(sys.argv[1]):
        print('No such file:', sys.argv[1])
        exit(2)

    ipfile = sys.argv[1]
    commands = sys.argv[2]
    password = getpass.getpass()

    # 打开文件，读取地址，执行命令
    with open(ipfile) as fobj:
        for line in fobj:
            ip = line.strip()  # 去除行尾的回车才是IP地址
            # rcmd(ip, passwd=password, commands=commands)
            t = threading.Thread(
                target=rcmd, args=(ip,),
                kwargs={'passwd': password, 'commands': commands}
            )
            t.start()  # rcmd(*args, **kwargs)
