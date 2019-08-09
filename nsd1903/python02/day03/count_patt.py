"用于统计在某个文件中，某些字段出现的次数"

import re

def count_patt(fname, patt):
    result = {}  # 结果保存到字典中
    cpatt = re.compile(patt)  # 将模式编译，以便获得更好的效率

    # 遍历文件，在每一行中匹配模式
    with open(fname) as fobj:
        for line in fobj:
            m = cpatt.search(line)
            if m:  # 匹配到的匹配对象是True，匹配不到返回None为False
                key = m.group()
                result[key] = result.get(key, 0) + 1

    return result

if __name__ == '__main__':
    fname = 'access_log'
    ip = '^(\d+\.){3}\d+'  # 192.168.1.15  12345.1.12345678.20
    br = 'Firefox|MSIE|Chrome'
    print(count_patt(fname, ip))
    print(count_patt(fname, br))
