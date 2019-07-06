def pop_it():
    print('pop')

def push_it():
    print('push')

def view_it():
    print('view')

def show_menu():
    # 把函数保存到字典中
    cmds = {'0': pop_it, '1': push_it, '2': view_it}
    prompt = """(0) 压栈
(1) 出栈
(2) 查询
(3) 退出
请选择(0/1/2/3): """

    while True:
        # 删除用户输入字符串两端的空格
        choice = input(prompt).strip()
        if choice not in ['0', '1', '2', '3']:
            print('无效输入，请重试')
            continue

        if choice == '3':
            print('Bye-bye')
            break

        cmds[choice]()  # 从字典中取出函数并调用

        # if choice == '0':
        #     push_it()
        # elif choice == '1':
        #     pop_it()
        # elif choice == '2':
        #     view_it()
        # else:
        #     print('bye-bye')
        #     break

if __name__ == '__main__':
    show_menu()
