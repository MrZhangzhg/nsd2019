astr = 'python'
alist = [10, 20, 30]
atuple = ('tom', 'jerry')
adict = {'name': 'bob', 'age': 20}

for ch in astr:
    print(ch)

for i in alist:
    print(i)

for name in atuple:
    print(name)

for key in adict:
    print('%s: %s' % (key, adict[key]))
