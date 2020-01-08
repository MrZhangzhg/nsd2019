def get_info(name, age):
    if not 0 < age < 120:
        raise ValueError('年龄超过范围(1~119)')
    print('%s is %d years old' % (name, age))

