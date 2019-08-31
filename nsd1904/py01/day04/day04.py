alist = ['bob', 'alice', 'tom', 'jerrey']

for i in range(len(alist)):    # 常用
    print(i, alist[i])

print('*' * 30)

print(list(enumerate(alist)))

for item in enumerate(alist):
    print(item)

print('*' * 30)

for i, name in enumerate(alist):   # 常用
    print(i, name)
