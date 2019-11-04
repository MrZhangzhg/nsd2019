def get_fname():
    '返回一个文件名字符串'

def get_content():
    '返回文件内容的字符串列表'

def wfile(fname, content):
    '将content中的内容写入文件fname中'

if __name__ == '__main__':
    fname = get_fname()
    content = get_content()
    wfile(fname, content)
