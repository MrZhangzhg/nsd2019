import sys

def copy(src_fname, dst_fname):
    src_fobj = open(src_fname, 'rb')
    dst_fobj = open(dst_fname, 'wb')

    while 1:
        data = src_fobj.read(4096)  # 从源文件中一次最多读4096字节

        if not data:         # data为空表示False，取反为True
            break

        dst_fobj.write(data)

    src_fobj.close()
    dst_fobj.close()

copy(sys.argv[1], sys.argv[2])
