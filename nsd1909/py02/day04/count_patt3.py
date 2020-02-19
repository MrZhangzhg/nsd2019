import re


class CountPatt:
    def __init__(self, fname):
        self.fname = fname

    def count_patt(self, patt):
        '用于在文件中统计每个模式字符串出现的次数'
        result = {}  # 定义用于保存结果的变量
        cpatt = re.compile(patt)  # 为了有更高的匹配效率，编译模式

        # 遍历文件，在每一行中匹配模式，匹配到了就更新到字典中
        with open(self.fname) as fobj:
            for line in fobj:
                m = cpatt.search(line)
                if m:  # 如果匹配到了内容
                    k = m.group()
                    result[k] = result.get(k, 0) + 1

        return result


if __name__ == '__main__':
    fname = 'access_log'
    ip = '^(\d+\.){3}\d+'  # 1234.56789.10.2  192.168.10.5
    br = 'Firefox|MSIE|Chrome'
    cp1 = CountPatt(fname)  # 创建实例
    result1 = cp1.count_patt(ip)
    print(result1)
    result2 = cp1.count_patt(br)
    print(result2)
