import os
import wget
import re
import urllib

def get_patt(fname, patt, encoding='utf8'):
    result = []
    cpatt = re.compile(patt)

    with open(fname, encoding=encoding) as fobj:
        for line in fobj:
            m = cpatt.search(line)
            if m:
                result.append(m.group())

    return result

if __name__ == '__main__':
    down_dir = '/tmp/163'
    # 如果目录不存在，则创建
    if not os.path.exists(down_dir):
        os.mkdir(down_dir)

    # 如果下载目录没有网易首页文件，则下载
    fname163 = '/tmp/163/163.html'
    url163 = 'http://www.163.com/'
    if not os.path.exists(fname163):
        wget.download(url163, fname163)

    # 取出网易首页中所有的图片网址
    img_patt = '(http|https)://[\w./-]+\.(png|jpg|jpeg|gif)'
    imgs = get_patt(fname163, img_patt, encoding='gbk')
    # print(imgs)
    for url in imgs:
        try:
            wget.download(url, down_dir)
        except urllib.error.HTTPError:
            pass
