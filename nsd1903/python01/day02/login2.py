import getpass

username = input('username: ')
password = getpass.getpass('password: ')

if username == 'bob' and password == '123456':
    print('\033[32;1mLogin successful\033[0m')
else:
    print('\033[31;1mLogin incorrect\033[0m')
