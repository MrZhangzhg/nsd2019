def push_it():
    print('push')

def pop_it():
    print('pop')

def view_it():
    print('view')

def show_menu():
    prompt = """(0) 压栈
(1) 出栈
(2) 查询
(3) 退出
请选择(0/1/2/3): """

    while 1:
        # 将用户输入字符去除两端空白字符后，赋值给choice
        choice = input(prompt).strip()
        if choice not in ['0', '1', '2', '3']:
            print('无效的输入，请重试。')
            continue

        if choice == '0':
            push_it()
        elif choice == '1':
            pop_it()
        elif choice == '2':
            view_it()
        else:
            print('\nBye-bye')
            break

if __name__ == '__main__':
    show_menu()
