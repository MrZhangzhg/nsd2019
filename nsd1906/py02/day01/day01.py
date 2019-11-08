import time

result = 0

start = time.time()
for i in range(1, 10000001):
    result += i
end = time.time()

print(result)
print(end - start)
