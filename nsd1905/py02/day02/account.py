import os
import pickle
from time import strftime

def save(fname):
    try:
        amount = int(input('金额: '))
        comment = input('备注: ')
    except ValueError:
        print('无效的金额')
        return
    except (KeyboardInterrupt, EOFError):
        print()
        return

    date = strftime('%Y-%m-%d')
    with open(fname, 'rb') as fobj:
        records = pickle.load(fobj)
    balance = records[-1][-2] + amount  # 最新余额

    record = [date, amount, 0, balance, comment]
    records.append(record)
    with open(fname, 'wb') as fobj:
        pickle.dump(records, fobj)

def cost(fname):
    try:
        amount = int(input('金额: '))
        comment = input('备注: ')
    except ValueError:
        print('无效的金额')
        return
    except (KeyboardInterrupt, EOFError):
        print()
        return

    date = strftime('%Y-%m-%d')
    with open(fname, 'rb') as fobj:
        records = pickle.load(fobj)
    balance = records[-1][-2] - amount  # 最新余额

    record = [date, 0, amount, balance, comment]
    records.append(record)
    with open(fname, 'wb') as fobj:
        pickle.dump(records, fobj)

def query(fname):
    # 取出所有的记录
    with open(fname, 'rb') as fobj:
        records = pickle.load(fobj)

    # 打印表头
    print('%-16s%-8s%-8s%-10s%-20s' % ('date', 'save', 'cost', 'balance', 'comment'))
    # 打印所有的记录
    for record in records:
        print('%-16s%-8s%-8s%-10s%-20s' % tuple(record))

def show_menu():
    cmds = {'0': save, '1': cost, '2': query}
    prompt = """(0) 收入
(1) 开销
(2) 查询
(3) 退出
请选择(0/1/2/3): """
    fname = 'account.data'
    init_data = [['2019-10-14', 0, 0, 10000, 'init']]

    # 如果记账文件不存，则初始化它
    if not os.path.exists(fname):
        with open(fname, 'wb') as fobj:
            pickle.dump(init_data, fobj)

    while 1:
        try:
            choice = input(prompt).strip()
        except (KeyboardInterrupt, EOFError):
            choice = '3'

        if choice not in ['0', '1', '2', '3']:
            print('无效的输入，请重试。')
            continue

        if choice == '3':
            print('\nBye-bye')
            break

        cmds[choice](fname)


if __name__ == '__main__':
    show_menu()
