import getpass   # 导入getpass模块

uname = input('username: ')
pwd = getpass.getpass('password: ')  # 调用getpass模块中getpass函数

if uname == 'bob' and pwd == '123456':
    print('登陆成功')
else:
    print('登陆失败')
