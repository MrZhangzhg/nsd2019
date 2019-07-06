import getpass

userdb = {}

def register():
    username = input('用户名: ')
    # 如果用户已存在则给出提示，否则读入密码并写入字典
    if username in userdb:
        print('\033[31;1m用户已存在\033[0m')
    else:
        password = input('密码: ')
        userdb[username] = password

def login():
    username = input('用户名: ')
    password = getpass.getpass('密码: ')
    # if username in userdb and userdb[username] == password:
    if userdb.get(username) == password:
        print('\033[32;1m登陆成功\033[0m')
    else:
        print('\033[31;1m登陆失败\033[0m')

def show_menu():
    cmds = {'0': register, '1': login}
    prompt = """(0) 注册
(1) 登陆
(2) 退出
请选择(0/1/2): """

    while True:
        # 将用户输入的两端空白去掉后，赋值给choice
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
