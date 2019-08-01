# 计算1到100之和
result = 0   # 声明变量用于保存结果
counter = 1   # 创建一个自增量，不断将其累加到result中

while counter < 101:
    result += counter   # result = result + counter
    counter += 1   # 计数器加1

print(result)
