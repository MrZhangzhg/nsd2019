stack = []

def push_it():
    try:
        item = input('数据: ').strip()
    except (KeyboardInterrupt, EOFError):
        print()   # 默认打印\n
        return    # 默认返回None。类似于循环的break, return会结束函数

    if item:
        stack.append(item)

def pop_it():
    if stack:
        print('\033[31;1m从表中弹出: %s\033[0m' % stack.pop())
    else:
        print('\033[31;1m空列表\033[0m')

def view_it():
    print('\033[32;1m%s\033[0m' % stack)

def show_menu():
    cmds = {'0': push_it, '1': pop_it, '2': view_it}
    prompt = """(0) 压栈
(1) 出栈
(2) 查询
(3) 退出
请选择(0/1/2/3): """

    while True:
        try:
            choice = input(prompt).strip()
        except (KeyboardInterrupt, EOFError):
            choice = '3'

        if choice not in ['0', '1', '2', '3']:
            print('无效的输入，请重试。')
            continue

        if choice == '3':
            print('\nBye-bye')
            break

        cmds[choice]()

if __name__ == '__main__':
    show_menu()
