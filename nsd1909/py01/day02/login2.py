import getpass  # 导入getpass模块

uname = input('username: ')
upass = getpass.getpass('password: ')  # 调用getpass模块中名为getpass的函数

if uname == 'bob' and upass == '123456':
    print('登陆成功')
else:
    print('登陆失败')
