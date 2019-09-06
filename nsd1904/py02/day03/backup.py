import os
import tarfile
import hashlib
import pickle
from time import strftime

def check_md5(fname):
    m = hashlib.md5()

    with open(fname, 'rb') as fobj:
        while True:
            data = fobj.read(4096)
            if not data:
                break
            m.update(data)

    return m.hexdigest()


def full_backup(src, dst, md5file):
    "打包src目录，并计算src目录下每个文件的md5值"
    # 拼接备份目标文件的绝对路径
    fname = "%s_full_%s.tar.gz" % (os.path.basename(src), strftime('%Y%m%d'))
    fname = os.path.join(dst, fname)

    # 实现完全备份，把src目录打包
    tar = tarfile.open(fname, 'w:gz')
    tar.add(src)
    tar.close()

    # 计算每个文件的md5值
    md5dict = {}
    for path, folders, files in os.walk(src):
        for file in files:
            key = os.path.join(path, file)
            md5dict[key] = check_md5(key)

    # 将md5字典存入文件
    with open(md5file, 'wb') as fobj:
        pickle.dump(md5dict, fobj)


def incr_backup(src, dst, md5file):
    # 拼接备份目标文件的绝对路径
    fname = "%s_incr_%s.tar.gz" % (os.path.basename(src), strftime('%Y%m%d'))
    fname = os.path.join(dst, fname)

    # 计算当前文件的md5值
    md5dict = {}
    for path, folders, files in os.walk(src):
        for file in files:
            key = os.path.join(path, file)
            md5dict[key] = check_md5(key)

    # 读取前一天的md5值
    with open(md5file, 'rb') as fobj:
        old_md5 = pickle.load(fobj)

    # 找出新增文件和已修改文件，进行备份
    tar = tarfile.open(fname, 'w:gz')
    for key in md5dict:
        if old_md5.get(key) != md5dict[key]:
            tar.add(key)
    tar.close()


if __name__ == '__main__':
    src = '/tmp/demo/security'
    dst = '/tmp/demo/backup'
    md5file = '/tmp/demo/backup/md5.data'
    if strftime('%a') == 'Mon':
        full_backup(src, dst, md5file)
    else:
        incr_backup(src, dst, md5file)
