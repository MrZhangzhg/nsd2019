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

def full_backup(src_dir, dst_dir, md5file):
    # 拼接出目标文件的绝对路径
    fname = os.path.basename(src_dir)
    fname = '%s_full_%s.tar.gz' % (fname, strftime('%Y%m%d'))
    fname = os.path.join(dst_dir, fname)

    # 完全备份，即把整个目录打包压缩
    tar = tarfile.open(fname, 'w:gz')
    tar.add(src_dir)
    tar.close()

    # 计算每个文件的md5值，保存到字典中
    md5dict = {}
    for path, folders, files in os.walk(src_dir):
        for file in files:
            key = os.path.join(path, file)
            md5dict[key] = check_md5(key)

    # 将md5字典保存到pickle存储器中
    with open(md5file, 'wb') as fobj:
        pickle.dump(md5dict, fobj)

def incr_backup(src_dir, dst_dir, md5file):
    # 拼接出目标文件的绝对路径
    fname = os.path.basename(src_dir)
    fname = '%s_incr_%s.tar.gz' % (fname, strftime('%Y%m%d'))
    fname = os.path.join(dst_dir, fname)

    # 计算每个文件的md5值，保存到字典中
    md5dict = {}
    for path, folders, files in os.walk(src_dir):
        for file in files:
            key = os.path.join(path, file)
            md5dict[key] = check_md5(key)

    # 取出前一天的md5值
    with open(md5file, 'rb') as fobj:
        old_md5 = pickle.load(fobj)

    # 备份新增的文件和已改动的文件
    tar = tarfile.open(fname, 'w:gz')
    for key in md5dict:
        if old_md5.get(key) != md5dict[key]:
            tar.add(key)
    tar.close()

    # 更新md5文件
    with open(md5file, 'wb') as fobj:
        pickle.dump(md5dict, fobj)

if __name__ == '__main__':
    src_dir = '/tmp/demo/security'
    dst_dir = '/tmp/demo'
    md5file = '/tmp/demo/md5.data'
    if strftime('%a') == 'Mon':
        full_backup(src_dir, dst_dir, md5file)
    else:
        incr_backup(src_dir, dst_dir, md5file)
