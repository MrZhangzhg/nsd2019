import os

def get_fname():
    '用于获取并返回文件名'
    while 1:
        fname = input('文件名: ')
        if not os.path.exists(fname):
            break
        print('文件已存在，请重试')

    return fname

def get_content():
    '用于获取并返回文件内容'
    

def wfile(fname, content):
    '用于将内容写入文件'

if __name__ == '__main__':
    fname = get_fname()
    content = get_content()
    wfile(fname, content)
