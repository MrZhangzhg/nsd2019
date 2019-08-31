def get_fname():
    "用于获取文件名"

def get_content():
    "用于获取文件内容"

def wfile(fname, content):
    "将content内容写到文件fname中"

if __name__ == '__main__':
    fname = get_fname()
    content = get_content()
    wfile(fname, content)
