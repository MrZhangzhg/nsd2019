import os

def get_fname():
    '用于获取文件名，返回一个不存在文件名'
    while 1:
        fname = input('文件名: ')
        # os.path.exists(fname)，如果文件已存在返回True，不存在返回False
        if not os.path.exists(fname):
            break
        print('文件已存在，请重试。')

    return fname

def get_content():
    '用于获取内容，返回一个列表'
    content = []  # 创建一个列表，用于存储用户输入内容

    print('请输入内容，在单独的一行输入end表示结束。')
    while 1:
        line = input('(end to quit)> ')
        if line == 'end':
            break

        # content.append(line + '\n')
        content.append(line)

    return content

def wfile(fname, content):
    '需要文件名和内容作为参数，将内容写入文件'
    with open(fname, 'w') as fobj:
        fobj.writelines(content)

if __name__ == '__main__':
    fname = get_fname()
    content = get_content()
    content = ['%s\n' % line for line in content]  # 给字串加上\n后，替换content变量
    wfile(fname, content)
