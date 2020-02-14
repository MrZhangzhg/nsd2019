# 写在函数外面的变量，是全局变量。全局变量从定义开始，到程序结束，一直可见可用。
stack = []

def push():
    '用于实现压栈功能'
    data = input('data: ').strip()  # 删除用户输入字符串两端的空格
    if data:  # 非空字符串为真，空为假
        stack.append(data)

def pop():
    '用于实现出栈功能'
    if stack:  # 非空列表为真，空为假
        print('从栈中，弹出: %s' % stack.pop())
    else:
        print('\033[31;1m空栈\033[0m')

def view():
    '实现查询功能'
    print(stack)

def show_menu():
    '用于实现菜单，根据用户的选择调用相应的函数'
    # 字典是容器类型，将函数保存到字典
    cmds = {'0': push, '1': pop, '2': view}
    prompt = '''(0) push
(1) pop
(2) view
(3) quit
Please input your choice(0/1/2/3): '''
    while 1:
        xuan = input(prompt).strip()  # 删除用户输入字符串两端的空格
        if xuan not in ['0', '1', '2', '3']:
            print('无效的选择，请重试。')
            continue

        if xuan == '3':
            print('Bye-bye')
            break

        cmds[xuan]()  # 在字典中取出函数，再加上()调用函数


if __name__ == '__main__':
    show_menu()
