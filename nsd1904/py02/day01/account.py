import os
import pickle

def save(fname):
    "收入"
    print('save')


def cost(fname):
    "开销"
    print('cost')


def query(fname):
    "查询"
    print('query')


def show_menu():
    "显示菜单"
    cmds = {'0': save, '1': cost, '2': query}
    prompt = """(0) 收入
(1) 开销
(2) 查询
(3) 退出
请选择(0/1/2/3): """

    # 定义记账文件，如果文件不存在，则写入初始化数据
    fname = 'account.data'
    init_data = [
        ['2019-9-4', 0, 0, 10000, 'init'],
    ]
    if not os.path.exists(fname):
        with open(fname, 'wb') as fobj:
            pickle.dump(init_data, fobj)

    while True:
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
