def rm_spaces(astr):
    # range(字符串长度)返回的数字正好是每个字符的下标
    for i in range(len(astr)):
        if astr[i] != ' ':   # 找到非空格字符的下标，中断循环
            break

    return astr[i:]   # 从非空格字符的下标开始切片

s1 = '    hello world'
result = rm_spaces(s1)
print(result)
