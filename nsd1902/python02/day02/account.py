import os
import pickle
from time import strftime

def save(fname):
    date = strftime('%Y-%m-%d')  # 日期
    amount = int(input('amount: '))  # 金额，float代替int可以有小数点
    comment = input('comment: ')  # 说明
    # 从文件中取出全部的收支记录
    with open(fname, 'rb') as fobj:
        records = pickle.load(fobj)
    balance = records[-1][-2] + amount   # 余额
    new_record = [date, amount, 0, balance, comment]
    records.append(new_record)  # 最新一笔收入追加到大列表中
    # 将更新后的列表写回文件
    with open(fname, 'wb') as fobj:
        pickle.dump(records, fobj)

def cost(fname):
    date = strftime('%Y-%m-%d')  # 日期
    amount = int(input('amount: '))  # 金额，float代替int可以有小数点
    comment = input('comment: ')  # 说明
    # 从文件中取出全部的收支记录
    with open(fname, 'rb') as fobj:
        records = pickle.load(fobj)
    balance = records[-1][-2] - amount  # 余额
    new_record = [date, 0, amount, balance, comment]
    records.append(new_record)  # 最新一笔收入追加到大列表中
    # 将更新后的列表写回文件
    with open(fname, 'wb') as fobj:
        pickle.dump(records, fobj)

def query(fname):
    # 打印表头
    print('%-12s%-8s%-8s%-12s%-15s' % ('date', 'save', 'cost', 'balance', 'comment'))
    # 取出数据
    with open(fname, 'rb') as fobj:
        records = pickle.load(fobj)

    for line in records:
        print('%-12s%-8s%-8s%-12s%-15s' % tuple(line))

def show_menu():
    cmds = {'0': save, '1': cost, '2': query}
    prompt = """(0) save
(1) cost
(2) query
(3) quit
Please input your choice(0/1/2/3): """
    fname = 'record.data'
    init_data = [
        ['2019-07-09', 0, 0, 10000, 'init'],
    ]
    # 如果还没有record.data文件，则创建
    if not os.path.exists(fname):
        with open(fname, 'wb') as fobj:
            pickle.dump(init_data, fobj)

    while True:
        choice = input(prompt).strip()
        if choice not in ['0', '1', '2', '3']:
            print('Invalid choice, try again.')
            continue

        if choice == '3':
            print('\nBye-bye')
            break

        cmds[choice](fname)

if __name__ == '__main__':
    show_menu()



