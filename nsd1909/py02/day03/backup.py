from time import strftime


def full_backup(src, dst, md5file):


def incr_backup(src, dst, md5file):


if __name__ == '__main__':
    src = '/tmp/demo/security'
    dst = '/tmp/demo/backup'
    md5file = '/tmp/demo/backup/md5.data'
    if strftime('%a') == 'Mon':
        full_backup(src, dst, md5file)
    else:
        incr_backup(src, dst, md5file)

# mkdir /tmp/demo
# cp -r /etc/security/ /tmp/demo
# mkdir /tmp/demo/backup


