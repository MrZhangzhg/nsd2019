import os
import pickle
from time import strftime


def save(fname):
    '记录收入'
    date = strftime('%Y-%m-%d')
    amount = int(input('金额: '))
    comment = input('备注: ')

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

def query(fname):
    '查询'

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
