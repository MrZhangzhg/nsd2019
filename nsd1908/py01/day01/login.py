user = input('username: ')
print('欢迎:', user)
print('欢迎: ' + user)
# '' % ()   => 字符串中包含变化数据，采用的方法
# 如果引号中只有一个变化数据，不用()  => '%s' % 10
# 如果引号中有多个变化数据，必须用()  => '%s is %s years old' % ('zs', 20)
print('欢迎: %s' % user)
