import re


def count_patt(fname, patt):
    '用于在文件中统计每个模式字符串出现的次数'
    result = {}  # 定义用于保存结果的变量
    cpatt = re.compile(patt)  # 为了有更高的匹配效率，编译模式

    # 遍历文件，在每一行中匹配模式，匹配到了就更新到字典中
    with open(fname) as fobj:
        for line in fobj:
            m = cpatt.search(line)
            if m:  # 如果匹配到了内容
                k = m.group()
                result[k] = result.get(k, 0) + 1
                # if k not in result:
                #     result[k] = 1
                # else:
                #     result[k] += 1

    return result


if __name__ == '__main__':
    fname = 'access_log'
    ip = '^(\d+\.){3}\d+'  # 1234.56789.10.2  192.168.10.5
    br = 'Firefox|MSIE'
    result1 = count_patt(fname, ip)
    result2 = count_patt(fname, br)
    # print(result1)
    l = list(result1.items())
    l.sort(key=lambda seq: seq[-1], reverse=True)
    print(l)
    print(result2)
