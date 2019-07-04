import os

def get_fname():
    while True:
        fname = input('filename: ')
        if not os.path.exists(fname):   # 判断文件如果不存在则中断
            break
        print('文件已存在，请重试。')

    return fname

def get_content():
    content = []

    print('请输入内容，输入end表示结束')
    while True:
        line = input('(end to quit)> ')
        if line == 'end':
            break
        content.append(line)

    return content

def wfile(fname, content):
    with open(fname, 'w') as fobj:
        fobj.writelines(content)

if __name__ == '__main__':
    fname = get_fname()
    content = get_content()
    content = ['%s\n' % line for line in content]
    wfile(fname, content)
