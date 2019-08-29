# sum100 = 0    # 创建变量用于保存计算结果
# counter = 0   # 创建计数器，用于累加到sum100
#
# while counter < 100:
#     counter += 1
#
#     if counter % 2 == 1:
#         continue
#     else:
#         sum100 += counter
#
# print(sum100)
#
#################################################
sum100 = 0    # 创建变量用于保存计算结果
counter = 0   # 创建计数器，用于累加到sum100

while counter < 100:
    counter += 1

    # if counter % 2 == 1:
    if counter % 2:  # 结果只有0或1，1为True，0为False
        continue

    sum100 += counter

print(sum100)
