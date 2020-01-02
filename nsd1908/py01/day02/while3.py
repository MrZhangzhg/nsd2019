result = 0
counter = 0

while counter < 100:
    counter += 1

    # if counter % 2 == 1:
    if counter % 2:  # counter % 2的值只有0或1，0为False，1为True
        continue

    result += counter

print(result)
