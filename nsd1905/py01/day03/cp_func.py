import sys

def copy(src_fname, dst_fname):
    with open(src_fname, 'rb') as src_fobj:
        with open(dst_fname, 'wb') as dst_fobj:
            while 1:
                data = src_fobj.read(4096)
                if not data:
                    break
                dst_fobj.write(data)

copy(sys.argv[1], sys.argv[2])
