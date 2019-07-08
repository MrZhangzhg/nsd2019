def set_age(name, age):
    if not 0 < age < 120:
        # 如果age没有在此范围抛出ValueError异常
        raise ValueError('年龄超出范围(1-120)')

    print('%s is %s years old.' % (name, age))

def set_age2(name, age):
    # 如果判断条件为False，将会发生AssertionError异常
    assert 0 < age < 120, '年龄超出范围(1-120)'
    print('%s is %s years old.' % (name, age))

if __name__ == '__main__':
    set_age('杨艳龙', 26)
    set_age2('李家豪', 222)
