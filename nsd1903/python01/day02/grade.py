score = int(input('分数: '))  # 将用户的输入转换为整数

if score >= 90:
    print('优')
elif score >= 80:
    print('好')
elif score >= 70:
    print('良')
elif score >= 60:
    print('及格')
else:
    print('你要努力了')

