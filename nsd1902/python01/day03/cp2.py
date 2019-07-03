# 本例非常重要

src_fname = '/bin/ls'
dst_fname = '/tmp/list2'

src_fobj = open(src_fname, 'rb')
dst_fobj = open(dst_fname, 'wb')

while True:
    data = src_fobj.read(4096)   # 每次最多读4096字节
    # if data == b'':
    # if len(data) == 0:   # len(b'') -> 0
    if not data:    # data值为b''，表示False
        break
    dst_fobj.write(data)

src_fobj.close()
dst_fobj.close()
