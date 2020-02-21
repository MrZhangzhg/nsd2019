from urllib import request

url = 'http://t1.hxzdhn.com/uploads/allimg/20150814/04r1cjow1zq.jpg'
fname = '/tmp/girl.jpg'

html = request.urlopen(url)
with open(fname, 'wb') as fobj:
    while 1:
        data = html.read(4096)
        if not data:
            break
        fobj.write(data)
