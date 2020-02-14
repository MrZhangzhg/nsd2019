def register():
    '用于注册新用户'
    print('注册')

def login():
    '用于实现用户登陆'
    print('登陆')

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
