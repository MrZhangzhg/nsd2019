def set_age(name, age):
    if not 0 < age < 120:
        raise ValueError('年龄超出正常范围')

    print('%s is %s years old' % (name, age))

if __name__ == '__main__':
    try:
        age = int(input('年龄: '))
        set_age('牛老师', age)
    except ValueError:
        print('请输入0~120之间的数字')
    except (KeyboardInterrupt, EOFError):
        print('\nBye-bye')
