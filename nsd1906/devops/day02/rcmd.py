import paramiko

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
    rcmd('192.168.1.10', passwd='123456', cmd='id root; id zhangsan')
