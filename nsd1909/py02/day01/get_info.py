def get_info(name, age):
    if not 1 <= age <=120:
        raise ValueError('年龄超出范围(1-120)')

    print('%s is %s years old' % (name, age))

if __name__ == '__main__':
    get_info('牛老师', 200)
