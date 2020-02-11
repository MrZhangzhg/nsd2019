# 该文件非常重要，将来有很多代码都采用这种形式

src_fname = '/bin/ls'
dst_fname = '/tmp/list'
src_fobj = open(src_fname, 'rb')
dst_fobj = open(dst_fname, 'wb')

while 1:
    data = src_fobj.read(4096)  # 从源文件中一次最多读4096字节

    # if data == b''     # 如果data为空
    # if len(data) == 0  # 如果data长度为0
    if not data:         # data为空表示False，取反为True
        break

    dst_fobj.write(data)

src_fobj.close()
dst_fobj.close()
