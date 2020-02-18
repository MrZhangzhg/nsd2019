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
    fname = '%s_full_%s.tar.gz' % (os.path.basename(src), strftime('%Y%m%d'))
    fname = os.path.join(dst, fname)

    # 打包压缩
    tar = tarfile.open(fname, 'w:gz')
    tar.add(src)
    tar.close()

    # 计算每个文件的md5值，保存到字典中
    md5dict = {}
    for path, folders, files in os.walk(src):
        for file in files:
            k = os.path.join(path, file)
            md5dict[k] = check_md5(k)

    # 将md5字典保存到文件中
    with open(md5file, 'wb') as fobj:
        pickle.dump(md5dict, fobj)

def incr_backup(src, dst, md5file):
    ''


if __name__ == '__main__':
    src = '/tmp/demo/security'
    dst = '/tmp/demo/backup'
    md5file = '/tmp/demo/backup/md5.data'
    if strftime('%a') != 'Mon':
        full_backup(src, dst, md5file)
    else:
        incr_backup(src, dst, md5file)

# mkdir /tmp/demo
# cp -r /etc/security/ /tmp/demo
# mkdir /tmp/demo/backup


