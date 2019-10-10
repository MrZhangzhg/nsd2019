stack = []

def push_it():
    data = input('数据: ').strip()
    if data:  # 字符串非空为True，追加到列表
        stack.append(data)

def pop_it():
    if stack:
        print('从栈中弹出: \033[31;1m%s\033[0m' % stack.pop())
    else:
        print('\033[34;1m栈已经是空的\033[0m')

def view_it():
    print('\033[32;1m%s\033[0m' % stack)

def show_menu():
    cmds = {'0': push_it, '1': pop_it, '2': view_it}
    prompt = '''(0) 压栈
(1) 出栈
(2) 查询
(3) 退出
请选择(0/1/2/3): '''
    while 1:
        choice = input(prompt).strip()  # 删除用户输出的额外的空格
        if choice not in ['0', '1', '2', '3']:
            print('无效输入，请重试。')
            continue

        if choice == '3':
            print('\nBye-bye')
            break

        cmds[choice]()

if __name__ == '__main__':
    show_menu()
