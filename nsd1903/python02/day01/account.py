import os
from time import strftime
import pickle

def save(fname):


def cost(fname):


def query(fname):


def show_menu():
    fname = 'account.data'
    init_data = [[strftime('%Y-%m-%d'), 0, 0, 10000, 'init']]
    # 如果记账文件不存在，则初始化它
    if not os.path.exists(fname):
        with open(fname, 'wb') as fobj:
            pickle.dump(init_data, fobj)

    cmds = {'0': save, '1': cost, '2': query}
    prompt = """(0) 收入
(1) 支出
(2) 查询
(3) 退出
请选择(0/1/2/3): """
    while True:
        choice = input(prompt).strip()
        if choice not in ['0', '1', '2', '3']:
            print('无效输入，请重试。')
            continue

        if choice == '3':
            print('\nBye-bye')
            break

        cmds[choice](fname)

if __name__ == '__main__':
    show_menu()
