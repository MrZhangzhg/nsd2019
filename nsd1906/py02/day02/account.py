import os
import pickle
from time import strftime


def save(fname):
    amount = int(input('金额: '))
    comment = input('备注: ')
    date = strftime('%Y-%m-%d')
    # 从文件中取出全部记录
    with open(fname, 'rb') as fobj:
        records = pickle.load(fobj)
    # 计算最新余额
    balance = records[-1][-2] + amount
    record = [date, amount, 0, balance, comment]
    records.append(record)
    # 把更新后的列表再次存入文件
    with open(fname, 'wb') as fobj:
        pickle.dump(records, fobj)

def cost(fname):
    amount = int(input('金额: '))
    comment = input('备注: ')
    date = strftime('%Y-%m-%d')
    # 从文件中取出全部记录
    with open(fname, 'rb') as fobj:
        records = pickle.load(fobj)
    # 计算最新余额
    balance = records[-1][-2] - amount
    record = [date, 0, amount, balance, comment]
    records.append(record)
    # 把更新后的列表再次存入文件
    with open(fname, 'wb') as fobj:
        pickle.dump(records, fobj)

def query(fname):
    # 取出全部的记录
    with open(fname, 'rb') as fobj:
        records = pickle.load(fobj)

    # 打印表头
    print(
        '%-12s%-8s%-8s%-12s%-20s' % ('date', 'save', 'cost', 'balance', 'comment')
    )
    # 打印记录
    for record in records:
        print('%-12s%-8s%-8s%-12s%-20s' % tuple(record))

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
