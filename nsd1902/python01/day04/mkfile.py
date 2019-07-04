import os

def get_fname():
    while True:
        fname = input('filename: ')
        if not os.path.exists(fname):   # 判断文件如果不存在则中断
            break
        print('文件已存在，请重试。')

    return fname

def get_content():
    pass

def wfile(fname, content):
    pass

if __name__ == '__main__':
    fname = get_fname()
    content = get_content()
    wfile(fname, content)
