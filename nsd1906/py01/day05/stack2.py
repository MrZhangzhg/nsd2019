stack = []

def push_it():
    # 读取用户输入，非空内容追加到列表，否则打印提示
    data = input('数据: ').strip()
    if data:  # 如果data非空
        stack.append(data)
    else:
        print('输入内容为空。')

def pop_it():
    if stack:
        print('从栈中，弹出: %s' % stack.pop())
    else:
        print('空栈')

def view_it():
    print(stack)

def show_menu():
    cmds = {'0': push_it, '1': pop_it, '2': view_it}
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

        if choice == '3':
            print('\nBye-bye')
            break

        cmds[choice]()

if __name__ == '__main__':
    show_menu()
