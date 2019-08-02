src_fname = '/bin/ls'
dst_fname = '/tmp/list'

src_fobj = open(src_fname, 'rb')
dst_fobj = open(dst_fname, 'wb')

while True:
    data = src_fobj.read(4096)
    # if len(data) == 0:
    # if data == b'':
    if not data:
        break

    dst_fobj.write(data)

src_fobj.close()
dst_fobj.close()


