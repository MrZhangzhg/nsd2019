import re


def count_patt(fname, patt):
    result = {}  # 保存结果
    cpatt = re.compile(patt)  # 编译模式，提升效率

    with open(fname) as fobj:
        for line in fobj:
            m = cpatt.search(line)
            if m:  # 如果匹配到了
                key = m.group()
                result[key] = result.get(key, 0) + 1

    return result


if __name__ == '__main__':
    fname = 'access_log'
    ip = '^(\d+\.){3}\d+'  # 12345.6789.1.232, 10.123.45.8
    br = 'Firefox|MSIE|Chrome'
    result1 = count_patt(fname, ip)
    result2 = count_patt(fname, br)
    print(result1)
    print(result2)
