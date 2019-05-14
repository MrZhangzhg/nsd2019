import os
import pickle

def save(fname):
    print('save')

def cost(fname):
    print('cost')

def query(fname):
    print('query')

def show_menu():
    cmds = {'0': save, '1': cost, '2': query}
    prompt = '''(0) 收入
(1) 支出
(2) 查询
(3) 退出
请选择(0/1/2/3): '''
    fname = 'account.data'
    if not os.path.exists(fname):
        init_data = [
            ['2019-05-13', 0, 0, 10000, 'init'],
        ]
        with open(fname, 'wb') as fobj:
            pickle.dump(init_data, fobj)

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
