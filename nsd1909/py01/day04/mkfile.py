def get_fname():
    '用于获取文件名，返回一个不存在文件名'

def get_content():
    '用于获取内容，返回一个列表'

def wfile(fname, content):
    '需要文件名和内容作为参数，将内容写入文件'

if __name__ == '__main__':
    fname = get_fname()
    content = get_content()
    wfile(fname, content)
