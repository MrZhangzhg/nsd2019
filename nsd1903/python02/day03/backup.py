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
    "完全备份需要打包目录和计算每个文件的md5值"
    # 备份的tar文件要有备份目录名、备份类型、时间
    fname = '%s_full_%s.tar.gz' % (os.path.basename(src), strftime('%Y%m%d'))
    fname = os.path.join(dst, fname)

    # 将源目录打包
    tar = tarfile.open(fname, 'w:gz')
    tar.add(src)
    tar.close()

    # 计算每个文件的md5值，将其存入字典
    md5dict = {}
    for path, folders, files in os.walk(src):
        for file in files:
            key = os.path.join(path, file)
            md5dict[key] = check_md5(key)

    # 通过pickle永久地把字典存到文件中
    with open(md5file, 'wb') as fobj:
        pickle.dump(md5dict, fobj)

def incr_backup(src, dst, md5file):
    "增量备份把新增文件和改动的文件打包；更新md5文件以便于后续比较"
    # 备份的tar文件要有备份目录名、备份类型、时间
    fname = '%s_incr_%s.tar.gz' % (os.path.basename(src), strftime('%Y%m%d'))
    fname = os.path.join(dst, fname)

    # 计算每个文件的md5值，将其存入字典
    md5dict = {}
    for path, folders, files in os.walk(src):
        for file in files:
            key = os.path.join(path, file)
            md5dict[key] = check_md5(key)

    # 取出前一天的md5值
    with open(md5file, 'rb') as fobj:
        old_md5 = pickle.load(fobj)

    # 将新增文件和有改动文件进行打包
    tar = tarfile.open(fname, 'w:gz')
    for key in md5dict:
        if old_md5.get(key) != md5dict[key]:
            tar.add(key)
    tar.close()

    # 更新md5字典文件
    with open(md5file, 'wb') as fobj:
        pickle.dump(md5dict, fobj)

if __name__ == '__main__':
    src = '/tmp/demo/security'
    dst = '/tmp/backup'
    md5file = '/tmp/backup/md5.data'
    if not os.path.isdir(dst):
        os.mkdir(dst)

    if strftime('%a') == 'Mon':
        full_backup(src, dst, md5file)
    else:
        incr_backup(src, dst, md5file)
