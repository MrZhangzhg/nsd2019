astr = 'hello'
alist = ['tom', 'jerry']
atuple = (10, 20, 30)
adict = {'name': 'tom', 'age': 22}
aset = set('abc')
fname = '/etc/passwd'

for ch in astr:
    print(ch)

for name in alist:
    print(name)

for i in atuple:
    print(i)

for key in adict:
    print('%s: %s' % (key, adict[key]))

for ch in aset:
    print(ch)

with open(fname) as fobj:
    for line in fobj:
        print(line)

