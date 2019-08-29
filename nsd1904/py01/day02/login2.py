import getpass

username = input('username: ')
# getpass.getpass是getpass模块中的一个功能也叫getpass
password = getpass.getpass('password: ')

if username == 'bob' and password == '123456':
    print('登陆成功')
else:
    print('登陆失败')
