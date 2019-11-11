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


# (nsd1906) [root@room8pc16 day03]# mkdir -p /tmp/demo/backup
# (nsd1906) [root@room8pc16 day03]# cp -r /etc/security /tmp/demo/


