import getpass

userdb = {}

def register():
    uname = input('username: ').strip()
    # 如果用户名非空，并且不是字典的key，要求输入密码
    if uname and (uname not in userdb):
        upass = input('password: ')
        userdb[uname] = upass
    else:
        print('用户名为空或已存在')

def login():
    uname = input('username: ')
    upass = getpass.getpass('password: ')
    # if (uname in userdb) and (userdb[uname] == upass):
    if userdb.get(uname) == upass:
        print('\033[32;1m登陆成功\033[0m')
    else:
        print('\033[31;1m登陆失败\033[0m')

def show_menu():
    cmds = {'0': register, '1': login}
    prompt = """(0) 注册
(1) 登陆
(2) 退出
请选择(0/1/2): """

    while 1:
        choice = input(prompt).strip()
        if choice not in ['0', '1', '2']:
            print('无效的输入，请重试。')
            continue

        if choice == '2':
            print('\nBye-bye')
            break

        cmds[choice]()

if __name__ == '__main__':
    show_menu()
