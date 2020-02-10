import random

# 定义人胜利的情况
win_list = [['石头', '剪刀'], ['剪刀', '布'], ['布', '石头']]

# 计算机随机选择
xuanxiang = ['石头', '剪刀', '布']
computer = random.choice(xuanxiang)

# 获取用户的输入
player = input('请出拳(石头/剪刀/布): ')

# 输出人机的选择
print('您: %s, 计算机: %s' % (player, computer))

# 判断胜负
if player == computer:
    print('平局')
elif [player, computer] in win_list:
    print('You WIN!!!')
else:
    print('You LOSE')

