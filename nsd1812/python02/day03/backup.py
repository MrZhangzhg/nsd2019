import os
import tarfile
from time import strftime

def full_backup(src_dir, dst_dir, md5file):
    # 拼接出目标文件的绝对路径
    fname = os.path.basename(src_dir)
    fname = '%s_full_%s.tar.gz' % (fname, strftime('%Y%m%d'))
    fname = os.path.join(dst_dir, fname)

    # 完全备份，即把整个目录打包压缩
    tar = tarfile.open(fname, 'w:gz')
    tar.add(src_dir)
    tar.close()

    

def incr_backup(src_dir, dst_dir, md5file):


if __name__ == '__main__':
    src_dir = '/tmp/demo/security'
    dst_dir = '/tmp/demo'
    md5file = '/tmp/demo/md5.data'
    if strftime('%a') == 'Mon':
        full_backup(src_dir, dst_dir, md5file)
    else:
        incr_backup(src_dir, dst_dir, md5file)
