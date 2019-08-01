# 100以内的偶数之和

# result = 0
# counter = 0
#
# while counter < 100:
#     counter += 1
#
#     if counter % 2 == 1:
#         continue
#     else:
#         result += counter
#######################################
# result = 0
# counter = 0
#
# while counter < 100:
#     counter += 1
#
#     if counter % 2 == 1:
#         continue
#
#     result += counter
#######################################

result = 0
counter = 0

while counter < 100:
    counter += 1

    if counter % 2:   # 求余只有0和1两种情况，非0为真，0为假
        continue

    result += counter
