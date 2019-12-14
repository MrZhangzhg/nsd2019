from urllib import request
import sys

def download(url, fname):
    html = request.urlopen(url)

    with open(fname, 'wb') as fobj:
        while 1:
            data = html.read(4096)
            if not data:
                break
            fobj.write(data)

if __name__ == '__main__':
    download(sys.argv[1], sys.argv[2])
# python download.py http://xxxx /tmp/xxxx
# eog /tmp/xxxx.jpg
