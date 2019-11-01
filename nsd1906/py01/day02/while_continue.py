# 计算100以内偶数之和
result = 0  # 创建变量用于保存累加的结果
counter = 0  # 创建计数器，将其值累加到result中

while counter < 100:
    counter += 1

    # if counter % 2 == 1:
    if counter % 2:  # 结果只有1或0，1为真，0为假
        continue

    result += counter

print(result)


