import wget
import os
import re
from urllib import error

def get_url(fname, patt, encoding=None):
    patt_list = []
    cpatt = re.compile(patt)
    with open(fname, encoding=encoding) as fobj:
        for line in fobj:
            m = cpatt.search(line)
            if m:
                patt_list.append(m.group())

    return patt_list

if __name__ == '__main__':
    img_dir = '/tmp/163'
    url163 = 'http://www.163.com'
    fname163 = '/tmp/163/163.html'
    # 如果不存在目录和网易首页文件，先创建并下载首页文件
    if not os.path.exists(img_dir):
        os.mkdir(img_dir)
    if not os.path.exists(fname163):
        wget.download(url163, fname163)

    # 获取网易首页上所有的图片URL
    img_patt = '(http|https)://[/\w.-]+\.(gif|png|jpg|jpeg)'
    img_list = get_url(fname163, img_patt, 'gbk')
    # print(img_list)

    # 下载图片
    for url in img_list:
        try:
            wget.download(url, img_dir)
        except error.HTTPError:
            pass
