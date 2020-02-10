n1 = 10
s1 = 'Python'

if n1 > 5:  # 判断条件为真才会执行相应的代码块
    print('yes')
    print('ok')

if 'to' not in s1:
    print('True')

if -0.0:
    print('任何值为0的数字都是假')

if 10:
    print('非0数字为真')

if ' ':
    print('空格字符也是一个字符，为真')

if '':
    print('字符串长度为0，为假')

if [10, 20]:
    print('非空列表，为真')

if (10, 20):
    print('非空元组，为真')

if {}:
    print('空字典，为假')

if None:  # None是关键字，相当于其他语言中的null，表示真空
    print('None也为假')

if not 0:
    print('0为假，取反为真')
