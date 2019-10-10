import getpass

userdb = {}

def register():
    uname = input('username: ').strip()
    if not uname:  # 用户名为空不能注册
        print('用户名不能为空。')
        return

    # 用户不存在时询问密码，并写入字典
    if uname in userdb:
        print('用户已存在')
    else:
        upass = input('password: ')
        userdb[uname] = upass

def login():
    uname = input('username: ').strip()
    upass = getpass.getpass('password: ')
    # 用户名在字典中，并且字典中的密码与登陆时填写的密码一样才成功
    # if uname in userdb and userdb[uname] == upass:
    if userdb.get(uname) == upass:
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
            print('无效的输入，请重试。')
            continue

        if choice == '2':
            print('\nBye-bye')
            break

        cmds[choice]()

if __name__ == '__main__':
    show_menu()
