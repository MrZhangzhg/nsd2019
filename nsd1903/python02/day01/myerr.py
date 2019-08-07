def set_info(name, age):
    # 如果年龄不在允许的范围内，使用raise触发异常，异常类型自行定义
    if not 0 < age < 120:
        raise ValueError('年龄超过范围')

    print('%s is %s years old' % (name, age))

def set_info2(name, age):
    # 如果年龄不在允许的范围内，发生断言异常AssertionError，否则什么也不发生
    assert 0 < age < 120, '年龄超过范围'

    print('%s is %s years old' % (name, age))

if __name__ == '__main__':
    set_info('tom', 22)
    set_info2('jerry', 200)
