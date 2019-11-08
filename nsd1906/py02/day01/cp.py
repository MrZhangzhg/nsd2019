# pip install tqdm
import os
import sys
from tqdm import tqdm

def copy(src_fname, dst_fname, length=4096):
    size = os.stat(src_fname).st_size
    times, extra = divmod(size, length)
    if extra:
        times += 1

    with open(src_fname, 'rb') as src_fobj:
        with open(dst_fname, 'wb') as dst_fobj:
            for i in tqdm(range(times)):
                data = src_fobj.read(length)
                dst_fobj.write(data)

if __name__ == '__main__':
    copy(sys.argv[1], sys.argv[2])
