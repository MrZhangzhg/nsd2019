stack = []

def push_it():
    data = input('数据: ').strip()
    if data:   # 非空字符串为真
        stack.append(data)
    else:
        print('\033[31;1m输入为空\033[0m')

def pop_it():
    if stack:  # 列表非空为真
        print('从栈中弹出了: \033[34;1m%s\033[0m' % stack.pop())
    else:
        print('\033[31;1m空栈\033[0m')

def view_it():
    print('\033[32;1m%s\033[0m' % stack)

def show_menu():
    prompt = """(0) 压栈
(1) 出栈
(2) 查询
(3) 退出
请选择(0/1/2/3): """

    while 1:
        choice = input(prompt).strip()  # 去除字符串两端空白字符
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
            print('Bye-bye')
            break


if __name__ == '__main__':
    show_menu()
