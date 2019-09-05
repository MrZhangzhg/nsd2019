import os
import pickle
from time import strftime

def save(fname):
    "收入"
    try:
        amount = int(input('金额: '))
        comment = input('备注: ')
    except ValueError:
        print('请输入金额')
        return   # 返回到主程序，后续代码不再执行
    except (KeyboardInterrupt, EOFError):
        print('\nBye-bye')
        exit()   # 程序遇到exit，将会彻底结束

    date = strftime('%Y-%m-%d')
    # 在记账文件中取出全部记录
    with open(fname, 'rb') as fobj:
        records = pickle.load(fobj)
    balance = records[-1][-2] + amount  # 计算最新余额

    # 生成最新的一笔收入，并追加到大列表中
    record = [date, amount, 0, balance, comment]
    records.append(record)

    # 把更新过的记账内容写回文件
    with open(fname, 'wb') as fobj:
        pickle.dump(records, fobj)


def cost(fname):
    "开销"
    try:
        amount = int(input('金额: '))
        comment = input('备注: ')
    except ValueError:
        print('请输入金额')
        return   # 返回到主程序，后续代码不再执行
    except (KeyboardInterrupt, EOFError):
        print('\nBye-bye')
        exit()   # 程序遇到exit，将会彻底结束

    date = strftime('%Y-%m-%d')
    # 在记账文件中取出全部记录
    with open(fname, 'rb') as fobj:
        records = pickle.load(fobj)
    balance = records[-1][-2] - amount  # 计算最新余额

    # 生成最新的一笔开销，并追加到大列表中
    record = [date, 0, amount, balance, comment]
    records.append(record)

    # 把更新过的记账内容写回文件
    with open(fname, 'wb') as fobj:
        pickle.dump(records, fobj)


def query(fname):
    "查询"
    # 取出所有的记录
    with open(fname, 'rb') as fobj:
        records = pickle.load(fobj)

    # 打印表头
    print('%-14s%-8s%-8s%-12s%-20s' % ('date', 'save', 'cost', 'balance', 'comment'))
    # 循环取出第一条记录并打印
    for record in records:
        print('%-14s%-8s%-8s%-12s%-20s' % tuple(record))

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
        try:
            choice = input(prompt).strip()
        except (KeyboardInterrupt, EOFError):
            choice = '3'  # 如果发生这两种异常，认为用户选了3

        if choice not in ['0', '1', '2', '3']:
            print('无效的输入，请重试。')
            continue

        if choice == '3':
            print('\nBye-bye')
            break

        cmds[choice](fname)


if __name__ == '__main__':
    show_menu()
