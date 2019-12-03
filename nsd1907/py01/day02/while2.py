# 1到100以内的偶数之和
result = 0
counter = 0

while counter < 100:
    counter += 1

    if counter % 2 == 1:
        continue
    else:
        result += counter

print(result)
