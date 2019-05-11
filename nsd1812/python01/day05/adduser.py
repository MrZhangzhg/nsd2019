import sys
import string
import random
import subprocess

all_chs = string.ascii_letters + string.digits

def gen_pass(n=8):
    result = [random.choice(all_chs) for i in range(n)]
    return ''.join(result)

def adduser(user, password, fname):
    info = '''用户信息：
用户名：%s
密码：%s
''' % (user, password)

    rc = subprocess.run(
        'id %s' % user,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    if rc.returncode == 0:
        print('%s已存在' % user)
        exit(1)  # 结束程序，$? => 1

    # 创建用户
    subprocess.run(
        'useradd %s' % user,
        shell=True
    )
    # 添加密码
    subprocess.run(
        'echo %s | passwd --stdin %s' % (password, user),
        shell=True
    )
    # 将用户名和密码写入文件
    with open(fname, 'a') as fobj:
        fobj.write(info)

if __name__ == '__main__':
    pwd = gen_pass()
    username = sys.argv[1]
    fname = '/tmp/users.txt'
    adduser(username, pwd, fname)
