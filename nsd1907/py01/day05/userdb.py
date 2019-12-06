import getpass

userdb = {}

def register():
    username = input('用户名: ').strip()
    if not username:
        print('用户名不能为空')
    elif username in userdb:
        print('用户已存在')
    else:
        password = input('密码: ')
        userdb[username] = password

def login():
    username = input('用户名: ').strip()
    password = getpass.getpass('密码: ')
    # if (username in userdb) and (userdb[username] == password):
    if userdb.get(username) == password:
        print('登陆成功')
    else:
        print('登陆失败')

def show_menu():
    cmds = {'0': register, '1': login}
    prompt = """(0) 注册
(1) 登陆
(2) 退出
请选择(0/1/2): """

    while 1:
        choice = input(prompt).strip()
        if choice not in ['0', '1', '2']:
            print('无效输入，请重试。')
            continue

        if choice == '2':
            print('Bye-bye')
            break

        cmds[choice]()

if __name__ == '__main__':
    show_menu()
