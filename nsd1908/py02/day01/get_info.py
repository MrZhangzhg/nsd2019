def get_info(name, age):
    if not 0 < age < 120:
        raise ValueError('年龄超过范围(1~119)')
    print('%s is %d years old' % (name, age))

def get_info2(name, age):
    # age在0到120之间什么也不会发生，如果不是，则发生AssertionError异常
    assert 0 < age < 120, '年龄超过范围(1~119)'
    print('%s is %d years old' % (name, age))

