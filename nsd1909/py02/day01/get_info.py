def get_info(name, age):
    if not 1 <= age <= 120:
        raise ValueError('年龄超出范围(1-120)')

    print('%s is %s years old' % (name, age))

def get_info2(name, age):
    # assert后面的表示式为真，则什么也不发生；否则，一定发生AssertionError
    assert 1 <= age <= 120, '年龄超出范围(1-120)'
    print('%s is %s years old' % (name, age))

if __name__ == '__main__':
    get_info('牛老师', 20)
    get_info2('牛老师', 200)
