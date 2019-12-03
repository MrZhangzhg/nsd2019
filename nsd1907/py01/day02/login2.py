import getpass   # 导入名为getpass的模块

uname = input('username: ')
# 调用getpass模块中的getpass函数
upass = getpass.getpass('password: ')

if uname == 'bob' and upass == '123456':
    print('登陆成功')
else:
    print('登陆失败')
