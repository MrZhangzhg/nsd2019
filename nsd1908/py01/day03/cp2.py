src_fname = '/bin/ls'
dst_fname = '/tmp/list2'
src_fobj = open(src_fname, 'rb')
dst_fobj = open(dst_fname, 'wb')

while 1:
    data = src_fobj.read(4096)
    # if len(data) == 0:
    # if data == b'':
    if not data:  # 如内容已经全读完，则读到的是空串，空为假，取反为真
        break
    dst_fobj.write(data)

src_fobj.close()
dst_fobj.close()
