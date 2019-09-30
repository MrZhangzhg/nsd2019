import random

all_choices = ['石头', '剪刀', '布']
win_list = [['石头', '剪刀'], ['剪刀', '布'], ['布', '石头']]
player = input('请出拳(石头/剪刀/布): ')
computer = random.choice(all_choices)

print('你选择了: %s, 计算机选择了: %s' % (player, computer))
if player == computer:
    print('平局')
elif [player, computer] in win_list:
    print('You WIN!!!')
else:
    print('You LOSE!!!')
