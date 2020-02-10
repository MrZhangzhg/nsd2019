# 计算100以内偶数之和
result = 0
i = 0

while i < 100:
    i += 1
    # if i % 2 == 1:   # 可以简化为下面写法
    if i % 2:          # i % 2的结果只能是1或0，1为真，0为假
        continue

    result += i

print(result)
