stack = []

def push_it():
    '用于实现压栈功能'
    data = input('数据: ').strip()
    if data:  # 非空字符串为True
        stack.append(data)
    else:
        print('\033[31;1m输入为空\033[0m')

def pop_it():
    '用于实现出栈功能'
    if stack:  # 列表非空为True
        print('从列表中，弹出了: \033[34;1m%s\033[0m' % stack.pop())
    else:
        print('\033[31;1m列表为空\033[0m')

def view_it():
    '用于实现查询功能'
    print('\033[32;1m%s\033[0m' % stack)

def show_menu():
    '用于在屏幕上打印菜单，根据用户选择，调用相关功能函数'
    cmds = {'0': push_it, '1': pop_it, '2': view_it}
    prompt = """(0) 压栈
(1) 出栈
(2) 查询
(3) 退出
请选择(0/1/2/3): """
    while 1:
        choice = input(prompt).strip()  # 将输入的两端空白字符删除
        if choice not in ['0', '1', '2', '3']:
            print('无效的选择，请重试。')
            continue

        if choice == '3':
            print('\nBye-bye')
            break

        cmds[choice]()

        # if choice == '0':
        #     push_it()
        # elif choice == '1':
        #     pop_it()
        # elif choice == '2':
        #     view_it()
        # else:
        #     print('\nBye-bye')
        #     break

if __name__ == '__main__':
    show_menu()
