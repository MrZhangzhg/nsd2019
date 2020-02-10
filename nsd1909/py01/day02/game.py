import random

# 计算机随机选择
xuanxiang = ['石头', '剪刀', '布']
computer = random.choice(xuanxiang)

# 获取用户的输入
player = input('请出拳(石头/剪刀/布): ')

# 输出人机的选择
print('您: %s, 计算机: %s' % (player, computer))

# 判断胜负
if player == '石头':
    if computer == '石头':
        print('平局')
    elif computer == '剪刀':
        print('You WIN!!!')
    else:
        print('You LOSE!!!')
elif player == '剪刀':
    if computer == '石头':
        print('You LOSE!!!')
    elif computer == '剪刀':
        print('平局')
    else:
        print('You WIN!!!')
else:
    if computer == '石头':
        print('You WIN!!!')
    elif computer == '剪刀':
        print('You LOSE!!!')
    else:
        print('平局')
