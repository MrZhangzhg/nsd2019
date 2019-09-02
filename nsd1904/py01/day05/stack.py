def push_it():
    "压栈"
    print('push')

def pop_it():
    "出栈"
    print('pop')

def view_it():
    "查询"
    print('view')

def show_menu():
    "显示菜单"
    prompt = """(0) 压栈
(1) 出栈
(2) 查询
(3) 退出
请选择(0/1/2/3): """
    while True:
        choice = input(prompt).strip()  # 去除输入的两端空白字符
        if choice not in ['0', '1', '2', '3']:
            print('无效选择，请重试！')
            continue

        if choice == '0':
            push_it()
        elif choice == '1':
            pop_it()
        elif choice == '2':
            view_it()
        else:
            print('Bye-bye')
            break


if __name__ == '__main__':
    show_menu()
