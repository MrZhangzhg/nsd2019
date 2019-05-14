import os
import pickle
from time import strftime

def save(fname):
    try:
        amount = int(input('金额: '))
        comment = input('备注: ')
    except (KeyboardInterrupt, EOFError, ValueError):
        print('\n无效输入，返回。')
        return

    date = strftime('%Y-%m-%d')
    with open(fname, 'rb') as fobj:
        records = pickle.load(fobj)
        balance = records[-1][-2] + amount

    record = [date, amount, 0, balance, comment]
    records.append(record)
    with open(fname, 'wb') as fobj:
        pickle.dump(records, fobj)

def cost(fname):
    try:
        amount = int(input('金额: '))
        comment = input('备注: ')
    except (KeyboardInterrupt, EOFError, ValueError):
        print('\n无效输入，返回。')
        return

    date = strftime('%Y-%m-%d')
    with open(fname, 'rb') as fobj:
        records = pickle.load(fobj)
        balance = records[-1][-2] - amount

    record = [date, 0, amount, balance, comment]
    records.append(record)
    with open(fname, 'wb') as fobj:
        pickle.dump(records, fobj)

def query(fname):
    print('%-12s%-8s%-8s%-12s%-20s' % ('date', 'save', 'cost', 'balance', 'comment'))

    with open(fname, 'rb') as fobj:
        records = pickle.load(fobj)

    for record in records:
        print('%-12s%-8s%-8s%-12s%-20s' % tuple(record))

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
        try:
            choice = input(prompt).strip()
        except (KeyboardInterrupt, EOFError):
            choice = '3'

        if choice not in ['0', '1', '2', '3']:
            print('无效的选择，请重试。')
            continue

        if choice == '3':
            print('\nBye-bye')
            break

        cmds[choice](fname)

if __name__ == '__main__':
    show_menu()
