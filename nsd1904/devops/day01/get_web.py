from urllib import request, error
import wget
import os
import re

def download(url, fname):
    html = request.urlopen(url)
    with open(fname, 'wb') as fobj:
        while True:
            data = html.read(4096)
            if not data:
                break
            fobj.write(data)

if __name__ == '__main__':
    dest = '/tmp/163'
    fname163 = '/tmp/163/163.html'
    if not os.path.exists(dest):
        os.makedirs(dest)
    if not os.path.exists(fname163):
        download('http://www.163.com', fname163)
    # 获取图片URL
    url_patt = '(http|https)://[-./\w]+\.(png|jpg|jpeg|gif)'
    img_urls = []  # 用于存储图片的网址
    patt = re.compile(url_patt)
    with open(fname163, encoding='gbk') as fobj:
        for line in fobj:
            m = patt.search(line)
            if m:
                img_urls.append(m.group())

    for url in img_urls:
        try:
            wget.download(url, dest)
        except error.HTTPError:
            pass
