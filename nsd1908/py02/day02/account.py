import os
import pickle
from time import strftime

def save(fname):
    '用于记录收入'
    amount = int(input('金额: '))
    comment = input('备注: ')
    date = strftime('%Y-%m-%d')
    # 取出全部的收支情况列表
    with open(fname, 'rb') as fobj:
        records = pickle.load(fobj)
    # 计算最新余额
    balance = records[-1][-2] + amount
    # 构建收入情况列表
    line = [date, amount, 0, balance, comment]
    records.append(line)
    # 将更新后的收支情况列表写回文件
    with open(fname, 'wb') as fobj:
        pickle.dump(records, fobj)

def cost(fname):
    '用于记录开销'


def query(fname):
    '用于查询收支情况'


def show_menu():
    cmds = {'0': save, '1': cost, '2': query}
    prompt = """(0) 收入
(1) 开销
(2) 查询
(3) 退出
请选择(0/1/2/3): """
    fname = 'account.data'
    init_data = [['2020-01-09', 0, 0, 10000, 'init data']]
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
