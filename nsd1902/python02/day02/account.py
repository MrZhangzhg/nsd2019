import os
import pickle

def save(fname):
    print('save')

def cost(fname):
    print('cost')

def query(fname):
    print('query')

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



