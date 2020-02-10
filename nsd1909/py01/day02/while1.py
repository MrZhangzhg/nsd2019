# 计算1加到100的结果

# 创建变量用于保存最终结果
result = 0
# 创建计数器
i = 1

# 循环累加，一直加到计数器的值为100
while i <= 100:
    result += i
    i += 1

print(result)

# result += i   # result = result + i -> result = 0 + 1
# i += 1        # i = 2
#
# result += i   # result = result + i -> result = 1 + 2
# i += 1        # i = 3
#
# result += i
# i += 1
