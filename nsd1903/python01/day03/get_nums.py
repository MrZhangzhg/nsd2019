def get_nums(astr):
    result = ''  # 创建变量用于保存最终结果

    for ch in astr:  # 遍历字符串
        if ch in '0123456789':   # 如果是数字则与result拼接
            result += ch

    return result

s1 = 'a12bcd89xf2340ll'
a = get_nums(s1)
print(a)
