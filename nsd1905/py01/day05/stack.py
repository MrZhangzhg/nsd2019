def push_it():
    print('push')

def pop_it():
    print('pop')

def view_it():
    print('view')

def show_menu():
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
