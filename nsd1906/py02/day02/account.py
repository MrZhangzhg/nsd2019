import os
import pickle
from time import strftime


def save(fname):

def cost(fname):

def query(fname):

def show_menu():
    cmds = {'0': save, '1': cost, '2': query}
    prompt = """(0) save
(1) cost
(2) query
(3) quit
Please input your choice(0/1/2/3): """
    fname = 'account.data'
    init_data = [
        [strftime('%Y-%m-%d'), 0, 0, 10000, 'init data']
    ]
    # 如果文件不存在，把初始化数据写进去
    if not os.path.exists(fname):
        with open(fname, 'wb') as fobj:
            pickle.dump(init_data, fobj)

    while 1:
        choice = input(prompt).strip()
        if choice not in ['0', '1', '2', '3']:
            print('无效的输入，请重试。')
            continue

        if choice == '3':
            print('\nBye-bye')
            break

        cmds[choice](fname)

if __name__ == '__main__':
    show_menu()
