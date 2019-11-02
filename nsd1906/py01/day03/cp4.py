import sys

def copy(src_fname, dst_fname):
    src_fobj = open(src_fname, 'rb')
    dst_fobj = open(dst_fname, 'wb')

    while 1:
        data = src_fobj.read(4096)
        if not data:  # 空串为假，取反为真
            break

        dst_fobj.write(data)

    src_fobj.close()
    dst_fobj.close()

if len(sys.argv) != 3:
    print('Usage: %s src dst' % sys.argv[0])
    exit(10)  # 程序遇到exit就会彻底结束，1是$?的值

copy(sys.argv[1], sys.argv[2])

# python cp4.py /etc/hosts /tmp/zj
