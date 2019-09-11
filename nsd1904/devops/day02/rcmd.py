import paramiko

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
    rcmd('192.168.4.4', passwd='123456', command='id root; id bob')
