def set_age(name, age):
    assert 0 < age < 120, '年龄超出正常范围'
    print('%s is %s years old' % (name, age))

if __name__ == '__main__':
    try:
        age = int(input('年龄: '))
        set_age('牛老师', age)
    except (ValueError, AssertionError) as e:
        print('错误:', e)
    except (KeyboardInterrupt, EOFError):
        print('\nBye-bye')


    # set_age('牛老师', 200)
