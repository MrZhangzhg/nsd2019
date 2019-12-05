def get_fname():
    '用于获取文件名'

def get_content():
    '用于获取内容'

def wfile(fname, content):
    '用于将内容content，写入文件fname'

if __name__ == '__main__':
    fname = get_fname()
    content = get_content()
    wfile(fname, content)
