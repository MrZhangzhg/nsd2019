# import time
#
# result = 0
#
# start = time.time()
# for i in range(1, 10000001):
#     result += i
# end = time.time()
#
# print(result)
# print(end - start)

def set_age(name, age):
    if not 0 < age < 120:
        raise ValueError('年龄超过范围')
    print('%s is %d years old' % (name, age))

def set_age2(name, age):
    assert 0 < age < 120, '年龄超过范围'
    print('%s is %d years old' % (name, age))

if __name__ == '__main__':
    # set_age('牛老师', 200)
    set_age2('牛老师', 200)










