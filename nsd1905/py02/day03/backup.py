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
    '完全备份：打包整个目录；计算每个文件的md5值'
    # 生成压缩包的绝对路径: /path/to/目录名_full_日期.tar.gz
    fname = os.path.basename(src)
    fname = '%s_full_%s.tar.gz' % (fname, strftime('%Y%m%d'))
    fname = os.path.join(dst, fname)

    # 打包
    tar = tarfile.open(fname, 'w:gz')
    tar.add(src)
    tar.close()

    # 计算每个文件的md5值
    md5dict = {}
    for path, folders, files in os.walk(src):
        for file in files:
            key = os.path.join(path, file)
            md5dict[key] = check_md5(key)

    # 把md5字典写入文件
    with open(md5file, 'wb') as fobj:
        pickle.dump(md5dict, fobj)

def incr_backup(src, dst, md5file):
    fname = os.path.basename(src)
    fname = '%s_incr_%s.tar.gz' % (fname, strftime('%Y%m%d'))
    fname = os.path.join(dst, fname)

    # 计算当前文件的md5值
    md5dict = {}
    for path, folders, files in os.walk(src):
        for file in files:
            key = os.path.join(path, file)
            md5dict[key] = check_md5(key)

    # 取出前一天的md5值
    with open(md5file, 'rb') as fobj:
        old_md5 = pickle.load(fobj)

    # 将新增的和改动的文件打包
    tar = tarfile.open(fname, 'w:gz')
    for key in md5dict:
        if old_md5.get(key) != md5dict[key]:
            tar.add(key)
    tar.close()

    # 将今天的md5值写到字典
    with open(md5file, 'wb') as fobj:
        pickle.dump(md5dict, fobj)


if __name__ == '__main__':
    src = '/tmp/demo/security'  # 需要备份的目录
    dst = '/tmp/demo/backup'    # 备份目标
    md5file = '/tmp/demo/backup/md5.data'  # md5值文件
    if strftime('%a') == 'Mon':
        full_backup(src, dst, md5file)
    else:
        incr_backup(src, dst, md5file)
