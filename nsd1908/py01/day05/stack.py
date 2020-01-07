
def push_it():
    '用于实现压栈功能'
    print('push')

def pop_it():
    '用于实现出栈功能'
    print('pop')

def view_it():
    '用于实现查询功能'
    print('view')

def show_menu():
    '用于在屏幕上打印菜单，根据用户选择，调用相关功能函数'
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

        if choice == '0':
            push_it()
        elif choice == '1':
            pop_it()
        elif choice == '2':
            view_it()
        else:
            print('\nBye-bye')
            break

if __name__ == '__main__':
    show_menu()
