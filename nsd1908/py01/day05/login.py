import getpass

userdb = {}

def register():
    '用于注册用户'
    user = input('用户名: ').strip()
    # 如果用户名字符串非空，并且用户没有注册过
    if user and (user not in userdb):
        passwd = input('密码: ')
        userdb[user] = passwd
    else:
        print('用户名为空或用户已存在')

def login():
    '用于验证登陆'
    user = input('用户名: ').strip()
    passwd = getpass.getpass('密码: ')
    # if user in userdb and userdb[user] == passwd:
    if userdb.get(user) == passwd:
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
            print('无效的输入，请重试')
            continue

        if choice == '2':
            print('\nBye-bye')
            break

        cmds[choice]()

if __name__ == '__main__':
    show_menu()
