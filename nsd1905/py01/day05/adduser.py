import sys
import randpass2
import subprocess

def adduser(uname, pwd, fname):
    # 判断用户是否已存在
    result1 = subprocess.run('id %s &> /dev/null' % uname, shell=True)
    if result1.returncode == 0:
        print('%s已存在。' % uname)
        return

    # 创建用户，设置密码
    subprocess.run('useradd %s' % uname, shell=True)
    subprocess.run('echo %s | passwd --stdin %s' % (pwd, uname), shell=True)

    # 将用户名和密码写入文件
    with open(fname, 'a') as fobj:
        fobj.write('用户名: %s\n密码: %s\n' % (uname, pwd))

if __name__ == '__main__':
    passwd = randpass2.mk_pwd()
    adduser(sys.argv[1], passwd, sys.argv[2])
