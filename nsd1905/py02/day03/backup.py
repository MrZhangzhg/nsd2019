from time import strftime

def full_backup(src, dst, md5file):


def incr_backup(src, dst, md5file):


if __name__ == '__main__':
    src = '/tmp/demo/security'  # 需要备份的目录
    dst = '/tmp/demo/backup'    # 备份目标
    md5file = '/tmp/demo/backup/md5.data'  # md5值文件
    if strftime('%a') == 'Mon':
        full_backup(src, dst, md5file)
    else:
        incr_backup(src, dst, md5file)
