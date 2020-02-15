import os

path = '/tmp/nsd1909'

# for data in os.walk(path):
#     print(data)

# for data in os.walk(path):
#     print('%s:' % data[0])
#     print(data[1])
#     print(data[2])

# for data in os.walk(path):
#     print('%s:' % data[0])
#     for zimulu in data[1]:
#         print('\033[34;1m%s\033[0m' % zimulu, end=' ')
#     for file in data[2]:
#         print(file, end=' ')
#     print('\n')

# 元组有3项，可以将这3项分别赋值给3个变量
for path, folders, files in os.walk(path):
    print('%s:' % path)
    for zimulu in folders:
        print('\033[34;1m%s\033[0m' % zimulu, end='\t')
    for file in files:
        print(file, end='\t')
    print('\n')

