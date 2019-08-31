import os


def get_fname():
    "用于获取文件名"
    while True:
        fname = input('filename: ')
        if not os.path.exists(fname):
            break

        print('%s 已存在，请重试。' % fname)

    return fname


def get_content():
    "用于获取文件内容"
    content = []

    print('请输入内容，单独一行输入end结束。')
    while True:
        line = input('> ')
        if line == 'end':
            break

        content.append(line)

    return content


def wfile(fname, content):
    "将content内容写到文件fname中"
    with open(fname, 'w') as fobj:
        fobj.writelines(content)


if __name__ == '__main__':
    fname = get_fname()
    content = get_content()
    content = ['%s\n' % line for line in content]
    wfile(fname, content)
