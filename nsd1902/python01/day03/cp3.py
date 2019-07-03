src_fname = '/bin/ls'
dst_fname = '/tmp/list2'

with open(src_fname, 'rb') as src_fobj:
    with open(dst_fname, 'wb') as dst_fobj:
        while True:
            data = src_fobj.read(4096)   # 每次最多读4096字节
            if not data:    # data值为b''，表示False
                break
            dst_fobj.write(data)

