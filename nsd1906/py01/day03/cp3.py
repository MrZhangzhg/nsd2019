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

copy('/etc/passwd', '/tmp/password')
copy('/etc/hosts', '/tmp/zhuji')
