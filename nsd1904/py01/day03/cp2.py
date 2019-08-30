src_fname = '/bin/ls'
dst_fname = '/tmp/list2'

src_fobj = open(src_fname, 'rb')
dst_fobj = open(dst_fname, 'wb')

while True:
    data = src_fobj.read(4096)  # 每次读4096字节
    # if data == b'':
    # if len(data) == 0:
    if not data:   # 如果文件已经读完，则break
        break

    dst_fobj.write(data)   # 将读入数据写入目标文件

src_fobj.close()
dst_fobj.close()
