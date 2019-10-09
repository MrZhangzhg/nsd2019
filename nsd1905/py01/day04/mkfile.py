import os

def get_fname():
    '返回文件名'
    while 1:
        fname = input('filename: ')
        if not os.path.exists(fname):  # 文件不存在则中断循环
            break
        print('文件已存在，请重试。')

    return fname

def get_content():
    '返回内容'
    content = []

    print('输请入内容，在单独的一行上输入end结束。')
    while 1:
        line = input('(end to quit)> ')
        if line == 'end':
            break
        content.append(line)

    return content

def wfile(fname, content):
    '将内容content写入文件fname'
    with open(fname, 'w') as fobj:
        fobj.writelines(content)

if __name__ == '__main__':
    fname = get_fname()
    content = get_content()
    content = ['%s\n' % line for line in content]
    wfile(fname, content)
