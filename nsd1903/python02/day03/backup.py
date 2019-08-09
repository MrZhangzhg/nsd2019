from time import strftime
import os

def full_backup(src, dst, md5file):


def incr_backup(src, dst, md5file):


if __name__ == '__main__':
    src = '/tmp/demo/security'
    dst = '/tmp/backup'
    md5file = '/tmp/backup/md5.data'
    if not os.path.isdir(dst):
        os.mkdir(dst)

    if strftime('%a') == 'Mon':
        full_backup(src, dst, md5file)
    else:
        incr_backup(src, dst, md5file)
