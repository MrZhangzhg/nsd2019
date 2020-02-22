import paramiko
import sys
import getpass
import os
import threading

def rcmd(host, user, passwd, port=22, cmds=None):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, username=user, password=passwd, port=port)
    stdin, stdout, stderr = ssh.exec_command(cmds)
    out = stdout.read()
    err = stderr.read()
    if out:   # 如果命令有输出
        print('[%s] \033[32;1mOUT\033[0m:\n%s' % (host, out.decode()))
    if err:   # 如果命令执行错误
        print('[%s] \033[31;1mERROR\033[0m:\n%s' % (host, err.decode()))
    ssh.close()

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: %s ipfile 'commands'" % sys.argv[0])
        exit(1)   # 1就是$?值
    if not os.path.isfile(sys.argv[1]):
        print('No such file:', sys.argv[1])
        exit(2)
    ipfile = sys.argv[1]
    passwd = getpass.getpass()
    cmds = sys.argv[2]
    with open(ipfile) as fobj:
        for line in fobj:
            ip = line.strip()  # 文件每一行是一个ip地址，但是要去除行尾的\n
            t = threading.Thread(target=rcmd, args=(ip, 'root', passwd, 22, cmds))
            t.start()
# python3 rcmd.py servers.txt 'sleep 3; id root'
