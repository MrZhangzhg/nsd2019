def set_info(name, age):
    if not 0 < age < 120:
        raise ValueError('年龄超过范围')

    print('%s is %d years old' % (name, age))

def set_info2(name, age):
    assert 0 < age < 120, '年龄超过范围'
    print('%s is %d years old' % (name, age))

if __name__ == '__main__':
    try:
        set_info('牛老师', 20)
    except ValueError as e:
        print('错误:', e)

    set_info2('牛老师', 200)
