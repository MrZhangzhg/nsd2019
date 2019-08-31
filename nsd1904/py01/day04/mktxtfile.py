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

def wfile(fname, content):
    "将content内容写到文件fname中"

if __name__ == '__main__':
    fname = get_fname()
    content = get_content()
    wfile(fname, content)
