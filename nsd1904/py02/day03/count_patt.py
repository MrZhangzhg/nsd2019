import re

def count_patt(fname, patt):
    cpatt = re.compile(patt)  # 为了效率，先编译模式
    result = {}  # 用于保存结果

    with open(fname) as fobj:
        for line in fobj:
            m = cpatt.search(line)
            if m:  # 如果匹配到，匹配对象表示真；没匹配到，返回None，表示假
                key = m.group()  # 取出匹配内容
                result[key] = result.get(key, 0) + 1

    return result


if __name__ == '__main__':
    fname = 'access_log'
    ip = '^(\d+\.){3}\d+'  # 192.168.1.15   1234.56789.1.12345678
    br = 'Chrome|Firefox|MSIE'
    print(count_patt(fname, ip))
    print(count_patt(fname, br))
