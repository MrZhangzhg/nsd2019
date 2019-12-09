def set_age(name, age):
    if not 0 < age < 120:
        raise ValueError('年龄超出正常范围')

    print('%s is %s years old' % (name, age))

if __name__ == '__main__':
    set_age('牛老师', 200)
