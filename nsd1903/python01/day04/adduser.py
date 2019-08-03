import sys
import randpass2  # 导入自己编写的模块
import subprocess

def adduser(username, password, fname):
    # 判断用户是否已经存在
    result = subprocess.run(
        'id %s' % username,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    if result.returncode == 0:
        print('%s已存在' % username)
        return False  # 函数遇到return就返回，不会再向下执行

    # 创建用户，并设置密码
    subprocess.run('useradd %s' % username, shell=True)
    subprocess.run(
        'echo %s | passwd --stdin %s' % (password, username),
        shell=True
    )

    # 写入用户信息到文件
    info = """user info:
username: %s
password: %s
""" % (username, password)
    with open(fname, 'a') as fobj:
        fobj.write(info)


if __name__ == '__main__':
    username = sys.argv[1]
    password = randpass2.randpass()
    fname = '/tmp/users.txt'
    adduser(username, password, fname)
