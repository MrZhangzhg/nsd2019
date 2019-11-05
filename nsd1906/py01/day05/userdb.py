def register():


def login():


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
