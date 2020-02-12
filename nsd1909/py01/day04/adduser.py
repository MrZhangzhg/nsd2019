import sys
import randchs2
import subprocess

def adduser(user, passwd, fname):
    '创建用户，设置密码，并将相关信息写入到fname文件中'
    # 判断用户是否存在，存在则返回
    result = subprocess.run('id %s &> /dev/null' % user, shell=True)
    if result.returncode == 0:
        print('用户已存在')
        return   # 函数的return类似于循环的break，它将结束函数，默认返回None

    # 创建用户
    subprocess.run('useradd %s' % user, shell=True)
    # 设置密码
    subprocess.run(
        'echo %s | passwd --stdin %s' % (passwd, user), shell=True
    )

    # 信息写入文件
    info = '''用户信息:
用户: %s
密码: %s
''' % (user, passwd)
    with open(fname, 'a') as fobj:
        fobj.write(info)

if __name__ == '__main__':
    user = sys.argv[1]
    passwd = randchs2.suijizifu()
    fname = sys.argv[2]
    adduser(user, passwd, fname)
