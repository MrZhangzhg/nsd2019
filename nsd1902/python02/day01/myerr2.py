def set_age(name, age):
    if not 0 < age < 120:
        raise ValueError('年龄超出范围(1-120)')

    print('%s is %s years old.' % (name, age))

if __name__ == '__main__':
    set_age('杨艳龙', 266)
