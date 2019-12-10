import os
import pickle
from time import strftime


def save(fname):
    '记录收入'
    date = strftime('%Y-%m-%d')
    try:
        amount = int(input('金额: '))
        comment = input('备注: ')
    except ValueError:
        print('输入的金额无效。')
        return
    except (KeyboardInterrupt, EOFError):
        print('\nBye-bye')
        exit(1)

    # 在fname文件中取出最新余额，加上当前收入金额，即为最新余额
    with open(fname, 'rb') as fobj:
        records = pickle.load(fobj)

    balance = records[-1][-2] + amount

    # 将最新记录添加到文件中
    record = [date, amount, 0, balance, comment]
    records.append(record)
    with open(fname, 'wb') as fobj:
        pickle.dump(records, fobj)


def cost(fname):
    '记录支出'
    date = strftime('%Y-%m-%d')
    try:
        amount = int(input('金额: '))
        comment = input('备注: ')
    except ValueError:
        print('输入的金额无效。')
        return
    except (KeyboardInterrupt, EOFError):
        print('\nBye-bye')
        exit(1)

    # 在fname文件中取出最新余额，减去当前收入金额，即为最新余额
    with open(fname, 'rb') as fobj:
        records = pickle.load(fobj)

    balance = records[-1][-2] - amount

    # 将最新记录添加到文件中
    record = [date, 0, amount, balance, comment]
    records.append(record)
    with open(fname, 'wb') as fobj:
        pickle.dump(records, fobj)

def query(fname):
    '查询'
    # 打印表头
    print('%-12s%-8s%-8s%-12s%-20s' % ('date', 'save', 'cost', 'balance', 'comment'))
    # print('%-12s%-8s%-8s%-12s%-20s' % ('日期', '收入', '开销', '余额', '备注'))

    # 取出全部记录
    with open(fname, 'rb') as fobj:
        records = pickle.load(fobj)

    # 打印记录
    for record in records:
        print('%-12s%-8s%-8s%-12s%-20s' % tuple(record))


def show_menu():
    cmds = {'0': save, '1': cost, '2': query}
    prompt = """(0) 收入
(1) 支出
(2) 查询
(3) 退出
请选择(0/1/2/3): """
    fname = 'account.data'
    init_data = [
        ['2019-12-10', 0, 0, 10000, 'init data']
    ]
    # 如果文件不存在，则创建并写入初始化数据
    if not os.path.exists(fname):
        with open(fname, 'wb') as fobj:
            pickle.dump(init_data, fobj)

    while 1:
        try:
            choice = input(prompt).strip()
        except (KeyboardInterrupt, EOFError):
            choice = '3'  # 发生这两种异常，算用户选了3

        if choice not in ['0', '1', '2', '3']:
            print('无效的输入，请重试。')
            continue

        if choice == '3':
            print('\nBye-bye')
            break

        cmds[choice](fname)

if __name__ == '__main__':
    show_menu()
