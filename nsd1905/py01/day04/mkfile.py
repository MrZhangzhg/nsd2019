def get_fname():
    '返回文件名'

def get_content():
    '返回内容'

def wfile(fname, content):
    '将内容content写入文件fname'

if __name__ == '__main__':
    fname = get_fname()
    content = get_content()
    wfile(fname, content)
