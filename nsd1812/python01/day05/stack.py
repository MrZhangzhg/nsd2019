stack = []

def push_it():
    item = input('数据: ').strip()
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
    # 将函数存到字典中
    cmds = {'0': push_it, '1': pop_it, '2': view_it}
    prompt = """(0) 压栈
(1) 出栈
(2) 查询
(3) 退出
请选择(0/1/2/3): """

    while True:
        choice = input(prompt).strip()
        if choice not in ['0', '1', '2', '3']:
            print('无效的输入，请重试。')
            continue

        if choice == '3':
            print('Bye-bye')
            break

        cmds[choice]()  # 在字典中取出函数，进行调用

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
