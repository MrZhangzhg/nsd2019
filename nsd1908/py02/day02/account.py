import os
import pickle
from time import strftime

def save(fname):
    '用于记录收入'
    try:
        amount = int(input('金额: '))
        comment = input('备注: ')
    except ValueError:
        print('无效的金额。')
        # 函数的return类似于循环的break，遇到return将结束函数
        return
    except (KeyboardInterrupt, EOFError):
        print('\nBye-bye')
        exit()

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
    try:
        amount = int(input('金额: '))
        comment = input('备注: ')
    except ValueError:
        print('无效的金额。')
        # 函数的return类似于循环的break，遇到return将结束函数
        return
    except (KeyboardInterrupt, EOFError):
        print('\nBye-bye')
        exit()

    date = strftime('%Y-%m-%d')
    # 取出全部的收支情况列表
    with open(fname, 'rb') as fobj:
        records = pickle.load(fobj)
    # 计算最新余额
    balance = records[-1][-2] - amount
    # 构建收入情况列表
    line = [date, 0, amount, balance, comment]
    records.append(line)
    # 将更新后的收支情况列表写回文件
    with open(fname, 'wb') as fobj:
        pickle.dump(records, fobj)

def query(fname):
    '用于查询收支情况'
    with open(fname, 'rb') as fobj:
        records = pickle.load(fobj)

    # 打印表头
    print('%-12s%-8s%-8s%-12s%-20s' % ('date', 'save', 'cost', 'balance', 'comment'))
    # 打印内容
    for line in records:
        print('%-12s%-8s%-8s%-12s%-20s' % tuple(line))


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
