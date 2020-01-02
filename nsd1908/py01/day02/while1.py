result = 0   # 定义用于存储结果的变量
counter = 1  # 定义计数器

# 计数器不断的自增，每个计数器的值都累加到result中
while counter <= 100:
    result += counter
    counter += 1

print(result)
