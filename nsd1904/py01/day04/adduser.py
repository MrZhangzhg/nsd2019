import sys
import randpass2
import subprocess

def add_user(username, password, fname):
    # 判断用户是否已存在
    result = subprocess.run(
        'id %s' % username, shell=True,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    if result.returncode == 0:
        print('%s 已存在' % username)
        # 函数遇到return就结束了，不再向下执行
        return

    # 创建用户，设置密码
    subprocess.run('useradd %s' % username, shell=True)
    subprocess.run(
        'echo %s | passwd --stdin %s' % (password, username),
        shell=True
    )

    # 将用户信息写入文件
    uinfo = """用户信息:
用户名:%s
密码:%s
""" % (username, password)
    with open(fname, 'a') as fobj:  # 文件以追加方式打开
        fobj.write(uinfo)


if __name__ == '__main__':
    username = sys.argv[1]
    password = randpass2.randpass()
    add_user(username, password, '/tmp/users.txt')
