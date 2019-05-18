import paramiko

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
    rcmd('192.168.4.4', pwd='123456', command='id root; id john')
