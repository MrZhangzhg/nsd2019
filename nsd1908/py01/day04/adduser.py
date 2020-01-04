import sys
import subprocess
from randpass2 import randpass

def add_user(user, passwd, fname):
    # 判断用户是否已存在
    result = subprocess.run('id %s &> /dev/null' % user, shell=True)
    if result.returncode == 0:
        print('用户已存在')
        # return类似于循环的break，函数遇到return就结束了
        return

    # 创建用户，添加密码
    subprocess.run('useradd %s' % user, shell=True)
    subprocess.run(
        'echo %s | passwd --stdin %s' % (passwd, user), shell=True
    )

    # 将用户名和密码写入文件
    # info = "username: %s\npassword: %s\n" % (user, passwd)
    info = """username: %s
password: %s
""" % (user, passwd)
    # 写入文件
    with open(fname, 'a') as fobj:
        fobj.write(info)


if __name__ == '__main__':
    user = sys.argv[1]
    fname = sys.argv[2]
    passwd = randpass()
    add_user(user, passwd, fname)
