sum100 = 0
counter = 0

while counter < 100:
    counter += 1

    # if counter % 2:   # 余数只可能是1或0，1为True，0为False
    if counter % 2 == 1:
        continue

    sum100 += counter

print(sum100)
