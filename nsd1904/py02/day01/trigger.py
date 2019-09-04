def set_age(name, age):
    if not 0 < age < 120:
        raise ValueError('年龄超过范围')
    print('%s is %s years old' % (name, age))

def set_age2(name, age):
    # assert后面的表达式必须为真，否则出现AssertionError
    assert 0 < age < 120, '年龄超过范围'
    print('%s is %s years old' % (name, age))

if __name__ == '__main__':
    try:
        set_age('牛老师', 188)
    except ValueError as e:
        print('错误: %s' % e)

    set_age2('牛老师', 200)
