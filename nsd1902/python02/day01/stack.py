stack = []

def pop_it():
    if stack:
        print('从栈中弹出: %s' % stack.pop())
    else:
        print('空栈')

def push_it():
    try:
        data = input('数据: ')
    except (KeyboardInterrupt, EOFError):
        print()
        return

    stack.append(data)

def view_it():
    print(stack)

def show_menu():
    cmds = {'0': pop_it, '1': push_it, '2': view_it}
    prompt = """(0) 出栈
(1) 压栈
(2) 查询
(3) 退出
请选择(0/1/2/3): """

    while True:
        try:
            choice = input(prompt).strip()
        except (KeyboardInterrupt, EOFError):
            choice = '3'

        if choice not in ['0', '1', '2', '3']:
            print('无效输入，请重试')
            continue

        if choice == '3':
            print('\nBye-bye')
            break

        cmds[choice]()  # 从字典中取出函数并调用

if __name__ == '__main__':
    show_menu()
