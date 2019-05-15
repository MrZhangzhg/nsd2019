from time import strftime


def full_backup(src_dir, dst_dir, md5file):


def incr_backup(src_dir, dst_dir, md5file):


if __name__ == '__main__':
    src_dir = '/tmp/demo/security'
    dst_dir = '/tmp/demo'
    md5file = '/tmp/demo/md5.data'
    if strftime('%a') == 'Mon':
        full_backup(src_dir, dst_dir, md5file)
    else:
        incr_backup(src_dir, dst_dir, md5file)
