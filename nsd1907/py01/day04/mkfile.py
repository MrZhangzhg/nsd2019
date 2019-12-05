import os

def get_fname():
    '用于获取文件名'
    while 1:
        fname = input('文件名: ')
        if not os.path.exists(fname):
            break
        print('文件已存在，请重试。')

    return fname

def get_content():
    '用于获取内容'
    content = []

    print('请输入文件内容，在单独的一行输入end结束。')
    while 1:
        line = input('(end to quit)> ')
        if line == 'end':
            break
        content.append(line)

    return content

def wfile(fname, content):
    '用于将内容content，写入文件fname'

if __name__ == '__main__':
    fname = get_fname()
    content = get_content()
    wfile(fname, content)
