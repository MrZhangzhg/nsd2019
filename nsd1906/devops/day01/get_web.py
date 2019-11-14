import wget
import os
import re

def get_url(fname, patt, encoding=None):
    result = []
    cpatt = re.compile(patt)

    with open(fname, encoding=encoding) as fobj:
        for line in fobj:
            m = cpatt.search(line)
            if m:
                result.append(m.group())

    return result


if __name__ == '__main__':
    img_dir = '/tmp/163'
    fname163 = '/tmp/163/163.html'
    url163 = 'http://www.163.com'
    # 如果不存在保存图片的目录，则创建
    if not os.path.exists(img_dir):
        os.mkdir(img_dir)

    # 如果网易首页文件不存在，则下载
    if not os.path.exists(fname163):
        wget.download(url163, fname163)

    # 取出网易首页中所有的图片地址
    img_patt = '(http|https)://[-\w/.]+\.(jpg|png|jpeg|gif)'
    # 网易网页使用的编码是gbk，不是utf8
    img_list = get_url(fname163, img_patt, 'gbk')
    # print(img_list)
    # 下载图片
    for url in img_list:
        wget.download(url, img_dir)
