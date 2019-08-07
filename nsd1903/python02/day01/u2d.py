"""
转换为windows换行格式

把源文件的每行结尾的空白字符删除，再拼接上\r\n
"""
import sys

def unix2dos(src, dst):
    with open(src) as src_fobj:
        with open(dst, 'w') as dst_fobj:
            for line in src_fobj:
                line = line.rstrip() + '\r\n'
                dst_fobj.write(line)

if __name__ == '__main__':
    unix2dos(sys.argv[1], sys.argv[2])
