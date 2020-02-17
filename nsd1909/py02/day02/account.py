import os
import pickle
from time import strftime

def save(fname):
    '用于记录收入'
    print('save')

def cost(fname):
    '用于记录支出'
    print('cost')

def query(fname):
    '用于查帐'
    print('query')

def show_menu():
    '用于展示主菜单'
    cmds = {'0': save, '1': cost, '2': query}
    prompt = '''(0) 收入
(1) 开销
(2) 查询
(3) 退出
请选择(0/1/2/3): '''
    fname = 'account.data'
    # 判断记账文件是否存在，如果不存在，初始化它
    chushi = [[strftime('%Y-%m-%d'), 0, 0, 10000, 'init data']]
    if not os.path.exists(fname):
        with open(fname, 'wb') as fobj:
            pickle.dump(chushi, fobj)
            
    while 1:
        xuan = input(prompt).strip()
        if xuan not in ['0', '1', '2', '3']:
            print('无效的输入，请重试。')
            continue

        if xuan == '3':
            print('\nBye-bye')
            break

        cmds[xuan](fname)

if __name__ == '__main__':
    show_menu()
