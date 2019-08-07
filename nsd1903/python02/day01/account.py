import os
from time import strftime
import pickle

def save(fname):
    amount = int(input('金额: '))
    comment = input('备注: ')
    date = strftime('%Y-%m-%d')
    # 取出所有的记录
    with open(fname, 'rb') as fobj:
        records = pickle.load(fobj)
    # 计算最新余额
    balance = records[-1][-2] + amount
    # 更新列表
    records.append([date, amount, 0, balance, comment])
    # 把列表再回写到文件
    with open(fname, 'wb') as fobj:
        pickle.dump(records, fobj)

def cost(fname):
    amount = int(input('金额: '))
    comment = input('备注: ')
    date = strftime('%Y-%m-%d')
    # 取出所有的记录
    with open(fname, 'rb') as fobj:
        records = pickle.load(fobj)
    # 计算最新余额
    balance = records[-1][-2] - amount
    # 更新列表
    records.append([date, 0, amount, balance, comment])
    # 把列表再回写到文件
    with open(fname, 'wb') as fobj:
        pickle.dump(records, fobj)

def query(fname):
    with open(fname, 'rb') as fobj:
        records = pickle.load(fobj)

    # 打印表头
    print('%-12s%-8s%-8s%-10s%-20s' % ('date', 'save', 'cost', 'balance', 'comment'))
    # 取出每个记录，打印
    for record in records:
        print('%-12s%-8s%-8s%-10s%-20s' % tuple(record))

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
