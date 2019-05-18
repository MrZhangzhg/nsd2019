import paramiko
import threading
import sys
import getpass
import os

def rcmd(host, user='root', pwd=None, port=22, command=None):
    ssh = paramiko.SSHClient()  # 实例化SSHClient
    # 设置自动接受密钥
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # 连接远程服务器
    ssh.connect(host, username=user, password=pwd, port=port)
    # 在远程服务器上执行命令
    stdin, stdout, stderr = ssh.exec_command(command)
    out = stdout.read()
    err = stderr.read()
    if out:  # 如果有输出，则打印在屏幕上
        print('[\033[32;1m%s\033[0m] OUT:\n%s' % (host, out.decode()))
    if err:
        print('[\033[31;1m%s\033[0m] ERROR:\n%s' % (host, err.decode()))
    ssh.close()  # 关闭连接

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: %s ipfile 'command_to_execute'" % sys.argv[0])
        exit(1)
    if not os.path.isfile(sys.argv[1]):
        print('No such file: %s' % sys.argv[1])
        exit(2)
    ipfile = sys.argv[1]
    command = sys.argv[2]
    pwd = getpass.getpass()
    with open(ipfile) as fobj:
        for line in fobj:
            ip = line.strip()  # 把一行文本两端的空白字符移除
            t = threading.Thread(target=rcmd, args=(ip,), kwargs={'pwd': pwd, 'command': command})
            t.start()  # target(*args, **kwargs)
