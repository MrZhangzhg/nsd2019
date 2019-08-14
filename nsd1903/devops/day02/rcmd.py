import paramiko


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
    hostfile = 'servers.txt'
    password = '123456'
    cmds = 'id root; id jerry'
    with open(hostfile) as fobj:
        for line in fobj:
            ip = line.strip()
            rcmd(ip, passwd=password, cmds=cmds)
