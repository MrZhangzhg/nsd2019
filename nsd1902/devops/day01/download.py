'下载https://www.jianshu.com首页中的所有图片'
import wget
import os
import re
from urllib import request

def get_web(url, fname):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}
    r = request.Request(url, headers=headers)
    js_index = request.urlopen(r)
    with open(fname, 'wb') as fobj:
        while True:
            data = js_index.read(4096)
            if not data:
                break
            fobj.write(data)

def get_urls(fname, patt):
    patt_list = []
    cpatt = re.compile(patt)

    with open(fname) as fobj:
        for line in fobj:
            m = cpatt.search(line)
            if m:
                patt_list.append(m.group())

    return patt_list


if __name__ == '__main__':
    # 将图片存到dst目录，如果目录不存在则创建
    dst = '/tmp/jianshu'
    if not os.path.exists(dst):
        os.mkdir(dst)

    # 通过urllib下载简书首页html文件
    get_web('https://www.jianshu.com/', '/tmp/js.html')

    # 在网页中找到所有的图片地址
    img_patt = '//[\w/.-]+\.(png|jpg|jpeg|gif)'
    imgs_list = get_urls('/tmp/js.html', img_patt)
    # print(imgs_list)
    for img_url in imgs_list:
        img_url = 'https:' + img_url
        wget.download(img_url, dst)

