result = 0
counter = 0

while counter < 100:
    counter += 1

    # if counter % 2 == 1:
    if counter % 2:  # counter % 2的结果只有1或0，1为真，0为假
        continue
    # else:
    #     result += counter
    result += counter

print(result)
