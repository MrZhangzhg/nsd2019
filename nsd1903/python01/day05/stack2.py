stack = []

def push_it():
    data = input('数据: ').strip()
    if data:
        stack.append(data)
    else:
        print('数据为空，未添加')

def pop_it():
    if stack:
        print('从栈中弹出: %s' % stack.pop())
    else:
        print('空栈')

def view_it():
    print(stack)

def show_menu():
    # 字典是容器类型，可以把任意对象存入，本例中存入函数
    cmds = {'0': push_it, '1': pop_it, '2': view_it}
    prompt = """(0) 压栈
(1) 出栈
(2) 查询
(3) 退出
请选择(0/1/2/3): """

    while True:
        choice = input(prompt).strip()  # 去掉字符串两端空白字符
        if choice not in ['0', '1', '2', '3']:
            print('无效输入，请重试。')
            continue

        if choice == '3':
            print('Bye-bye')
            break

        cmds[choice]()  # 在字典中取出相应的函数进行调用

if __name__ == '__main__':
    show_menu()
