import os

def get_fname():
    while True:
        fname = input('文件名: ')
        # os.path.exists(fname) => 文件已存在返回True
        if not os.path.exists(fname):
            break
        print('文件已存在，请重试')

    return fname

def get_content():
    content = []

    print('请输入内容，输入end结束输入：')
    while True:
        line = input('(end to quit)> ')
        if line == 'end':
            break
        content.append(line + '\n')

    return content

def wfile(fname, content):
    with open(fname, 'w') as fobj:
        fobj.writelines(content)

if __name__ == '__main__':
    fname = get_fname()
    content = get_content()
    wfile(fname, content)
