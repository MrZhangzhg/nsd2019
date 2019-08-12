import wget
import os
from urllib import request

def download(url, fname):
    html = request.urlopen(url)
    with open(fname, 'wb') as fobj:
        while True:
            data = html.read(4096)
            if not data:
                break
            fobj.write(data)

if __name__ == '__main__':
    download_dir = '/tmp/163'
    if not os.path.exists(download_dir):
        os.mkdir(download_dir)

    url163 = 'http://www.163.com'
    fname163 = '/tmp/163/163.html'
    download(url163, fname163)



