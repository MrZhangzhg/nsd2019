username = input('用户名: ')
print('Welcome', username)
print("Welcome %s" % username)  # 程序将会使用username的值替换%s

# '' % ()   # 这是字符串替换的基本形式
# 'hello %s' % 'tom'   # 只有一个%s，后面的()可以省略
# '%s is %s years old' % ('tom', 20)
