# (nsd1907) [root@room8pc16 day03]# mkdir -p /tmp/demo/backup
# (nsd1907) [root@room8pc16 day03]# cp -r /etc/security/ /tmp/demo/
# 将security备份到backup
from time import strftime
import os
import tarfile
import hashlib
import pickle

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
    "源目录打包，计算每个文件的md5值"
    # 拼接出打包的文件名
    fname = '%s_full_%s.tar.gz' % \
            (os.path.basename(src), strftime('%Y%m%d'))
    fname = os.path.join(dst, fname)

    # 压缩
    tar = tarfile.open(fname, 'w:gz')
    tar.add(src)
    tar.close()

    # 计算每个文件的md5值
    md5dict = {}
    for path, folders, files in os.walk(src):
        for file in files:
            key = os.path.join(path, file)
            md5dict[key] = check_md5(key)

    # 把md5字典存到文件中
    with open(md5file, 'wb') as fobj:
        pickle.dump(md5dict, fobj)

def incr_backup(src, dst, md5file):
    "找到新增文件和改动的文件，将它们打包；更新md5值"
    # 拼接出打包的文件名
    fname = '%s_incr_%s.tar.gz' % \
            (os.path.basename(src), strftime('%Y%m%d'))
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

    # 将新增文件和变化文件打包
    tar = tarfile.open(fname, 'w:gz')
    for key in md5dict:
        if old_md5.get(key) != md5dict[key]:
            tar.add(key)
    tar.close()

    # 更新md5文件
    with open(md5file, 'wb') as fobj:
        pickle.dump(md5dict, fobj)


if __name__ == '__main__':
    src = '/tmp/demo/security'
    dst = '/tmp/demo/backup'
    md5file = '/tmp/demo/md5.data'
    # 周一完全备份，其他时间增量备份
    if strftime('%a') == 'Mon':
        full_backup(src, dst, md5file)
    else:
        incr_backup(src, dst, md5file)
