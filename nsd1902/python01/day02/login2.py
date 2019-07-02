import getpass  # 导入模块

username = input('username: ')
password = getpass.getpass('password: ')

if username == 'bob' and password == '123456':
    print('Login successful')
else:
    print('Login incorrect')
