if -0.0:
    print('值为假，不打印')

if 100:
    print('数字100，非0为真，打印')

if ' ':
    print('空格也是一个字符，所以是非空字符串，为真')

if []:
    print('空列表，为假')

if (1, 2, 3):
    print('非空元组，为真')

if {'name': 'bob'}:
    print('非空字典，为真')

if not None:
    print('None为假，取反为真')

if not 0:
    print('0为假，取反为真')

if not 'abcd':
    print('非空字符串为真，取反为假')
