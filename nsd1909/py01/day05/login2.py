import getpass

userdb = {}  # 用于保存用户名和密码的字典

def register():
    '用于注册新用户'
    username = input('用户: ').strip()
    # 如果用户名非空，并且不是字典的key，则提示输入密码
    if username and (username not in userdb):
        password = input('密码: ')
        userdb[username] = password
    else:
        print('用户名为空或用户已存在')

def login():
    '用于实现用户登陆'
    username = input('用户: ')
    password = getpass.getpass('密码: ')
    # 用户名不存在字典中，或者字典中的密码和用户登陆时填写的密码不一样，则为失败
    # if (username not in userdb) or (userdb[username] != password):
    if userdb.get(username) != password:
        print('登陆失败')
    else:
        print('登陆成功')

def show_menu():
    '用于打印菜单，根据用户选择调用相关函数'
    cmds = {'0': register, '1': login}
    prompt = '''(0) 注册
(1) 登陆
(2) 退出
请选择(0/1/2): '''
    while 1:
        xuan = input(prompt).strip()
        if xuan not in ['0', '1', '2']:
            print('无效的选择，请重试。')
            continue

        if xuan == '2':
            print('Bye-bye')
            break

        cmds[xuan]()

if __name__ == '__main__':
    show_menu()
