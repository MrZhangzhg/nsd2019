def save(fname):


def cost(fname):


def query(fname):


def show_menu():
    cmds = {'0': save, '1': cost, '2': query}
    prompt = '''(0) 收入
(1) 支出
(2) 查询
(3) 退出
请选择(0/1/2/3): '''
    fname = 'account.data'
    
    while True:
        choice = input(prompt).strip()
        if choice not in ['0', '1', '2', '3']:
            print('无效的选择，请重试。')
            continue

        if choice == '3':
            print('\nBye-bye')
            break

        cmds[choice](fname)

if __name__ == '__main__':
    show_menu()
