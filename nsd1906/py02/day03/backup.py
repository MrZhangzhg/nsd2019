import os
import tarfile
import hashlib
import pickle
from time import strftime

def check_md5(fname):
    '计算文件md5值的函数，接收文件名，返回md5值'
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
    fname = os.path.basename(src)
    fname = '%s_full_%s.tar.gz' % (fname, strftime('%Y%m%d'))
    fname = os.path.join(dst, fname)

    # 完全备份，就是把整个目录压缩
    tar = tarfile.open(fname, 'w:gz')
    tar.add(src)
    tar.close()

    # 计算每个文件的md5值
    md5dict = {}
    for path, folders, files in os.walk(src):
        for file in files:
            key = os.path.join(path, file)
            md5dict[key] = check_md5(key)

    # 将md5值存入文件
    with open(md5file, 'wb') as fobj:
        pickle.dump(md5dict, fobj)

def incr_backup(src, dst, md5file):
    # 拼接出备份文件的绝对路径
    fname = os.path.basename(src)
    fname = '%s_incr_%s.tar.gz' % (fname, strftime('%Y%m%d'))
    fname = os.path.join(dst, fname)

    # 计算每个文件的md5值
    md5dict = {}
    for path, folders, files in os.walk(src):
        for file in files:
            key = os.path.join(path, file)
            md5dict[key] = check_md5(key)

    # 取出前一天的md5值
    with open(md5file, 'rb') as fobj:
        old_md5 = pickle.load(fobj)

    # 找出新增文件和改动的文件进行备份
    tar = tarfile.open(fname, 'w:gz')
    for key in md5dict:
        if md5dict[key] != old_md5.get(key):
            tar.add(key)
    tar.close()

    # 更新md5文件
    with open(md5file, 'wb') as fobj:
        pickle.dump(md5dict, fobj)

if __name__ == '__main__':
    src = '/tmp/demo/security'
    dst = '/tmp/demo/backup'
    md5file = '/tmp/demo/backup/md5.data'
    if strftime('%a') != 'Mon':
        full_backup(src, dst, md5file)
    else:
        incr_backup(src, dst, md5file)


# (nsd1906) [root@room8pc16 day03]# mkdir -p /tmp/demo/backup
# (nsd1906) [root@room8pc16 day03]# cp -r /etc/security /tmp/demo/


