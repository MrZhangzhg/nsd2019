def get_fname():
    '用于获取并返回文件名'

def get_content():
    '用于获取并返回文件内容'

def wfile(fname, content):
    '用于将内容写入文件'

if __name__ == '__main__':
    fname = get_fname()
    content = get_content()
    wfile(fname, content)
