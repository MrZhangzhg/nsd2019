import sys
import subprocess
import randpass2


def adduser(uname, passwd, fname):
    # 判断用是否已存在
    reuslt = subprocess.run(
        'id %s &> /dev/null' % uname, shell=True
    )
    if reuslt.returncode == 0:
        print('用户已存在')
        # 函数遇到return就结束了，不会再向下执行
        return

    # 创建用户、设置密码
    subprocess.run('useradd %s' % uname, shell=True)
    subprocess.run(
        'echo %s | passwd --stdin %s' % (passwd, uname),
        shell=True
    )

    # 用户名和密码写到文件中
    info = '''用户名: %s
密码: %s
''' % (uname, passwd)
    with open(fname, 'a') as fobj:
        fobj.write(info)


if __name__ == '__main__':
    uname = sys.argv[1]
    fname = sys.argv[2]
    passwd = randpass2.randpass()
    adduser(uname, passwd, fname)
    # python adduser.py zs /tmp/users.txt
