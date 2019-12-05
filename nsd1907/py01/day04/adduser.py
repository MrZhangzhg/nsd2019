import sys
import randpass2
import subprocess

def add_user(user, passwd, fname):
    # 如果用户已存在，则返回，不要继续执行函数
    result = subprocess.run(
        'id %s &> /dev/null' % user, shell=True
    )
    if result.returncode == 0:
        print('用户已存在。')
        # return默认返回None，类似于break，函数遇到return也会提前结束
        return

    # 创建用户，设置密码
    subprocess.run(
        'useradd %s' % user, shell=True
    )
    subprocess.run(
        'echo %s | passwd --stdin %s' % (passwd, user),
        shell=True
    )

    # 写入文件
    info = """用户信息:
用户名: %s
密码: %s
""" % (user, passwd)
    with open(fname, 'a') as fobj:
        fobj.write(info)

if __name__ == '__main__':
    user = sys.argv[1]
    passwd = randpass2.randpass()
    fname = sys.argv[2]
    add_user(user, passwd, fname)

# python adduser.py tom /tmp/users.txt
