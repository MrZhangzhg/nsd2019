stack = []

def push_it():
    "压栈"
    data = input('数据: ').strip()
    if data:   # 如果输入的是非空字符串，则追加到列表
        stack.append(data)

def pop_it():
    "出栈"
    if stack:
        print('\033[31;1m从栈中弹出: %s\033[0m' % stack.pop())
    else:
        print('\033[31;1m空栈\033[0m')

def view_it():
    "查询"
    print("\033[33;1m%s\033[0m" % stack)

def show_menu():
    "显示菜单"
    # 注意，函数后面不要有括号，是把函数放到字典中，不是把函数的执行结果放进去
    cmds = {'0': push_it, '1': pop_it, '2': view_it}
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

        if choice == '3':
            print('Bye-bye')
            break

        cmds[choice]()

        # if choice == '0':
        #     push_it()
        # elif choice == '1':
        #     pop_it()
        # elif choice == '2':
        #     view_it()
        # else:
        #     print('Bye-bye')
        #     break


if __name__ == '__main__':
    show_menu()
