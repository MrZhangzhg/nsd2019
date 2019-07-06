def register():
    print('register')

def login():
    print('login')

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
            print('Bye-buy')
            break

        cmds[choice]()

if __name__ == '__main__':
    show_menu()
