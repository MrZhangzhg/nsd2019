import os
import tarfile
import hashlib
import pickle
from time import strftime

def check_md5(fname):
    m = hashlib.md5()

    with open(fname, 'rb') as fobj:
        while 1:
            data = fobj.read(4096)
            if not data:
                break
            m.update(data)

    return m.hexdigest()


def full_backup(src, dst, md5file):
    # 拼接出备份文件的绝对路径
    fname = os.path.basename(src)  # security
    fname = '%s_full_%s.tar.gz' % (fname, strftime('%Y%m%d'))
    fname = os.path.join(dst, fname)

    # 压缩
    tar = tarfile.open(fname, 'w:gz')
    tar.add(src)
    tar.close()

    # 计算每个文件的md5值，将其保存到字典
    md5dict = {}
    for path, folders, files in os.walk(src):
        for file in files:
            key = os.path.join(path, file)
            md5dict[key] = check_md5(key)

    # 将字典存入文件
    with open(md5file, 'wb') as fobj:
        pickle.dump(md5dict, fobj)


def incr_backup(src, dst, md5file):


if __name__ == '__main__':
    src = '/tmp/nsd1908/security'
    dst = '/tmp/nsd1908/backup'
    md5file = '/tmp/nsd1980/md5.data'
    if strftime('%a') == 'Mon':
        full_backup(src, dst, md5file)
    else:
        incr_backup(src, dst, md5file)


# (nsd1908) [root@room8pc16 day03]# cp -r /etc/security /tmp/nsd1908/
# 将security目录备份到backup目录
# (nsd1908) [root@room8pc16 day03]# ls /tmp/nsd1908/
# backup  security
