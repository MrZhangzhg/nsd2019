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
    url_163 = 'http://www.163.com'
    fname_163 = '/tmp/163.html'
    dst_dir = '/tmp/163'
    if not os.path.exists(fname_163):
        wget.download(url_163, fname_163)
    if not os.path.exists(dst_dir):
        os.mkdir(dst_dir)

    img_patt = '(http|https)://[-\w./]+\.(jpg|jpeg|png|gif)'
    # 注意网易网站的字符编码用的是“简体中文”，而不是utf8，所以编码要用gbk
    img_urls = get_url(fname_163, img_patt, 'gbk')
    # print(img_urls)
    for url in img_urls:
        try:
            wget.download(url, dst_dir)
        except:
            pass
