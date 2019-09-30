import random

all_choices = ['石头', '剪刀', '布']
win_list = [['石头', '剪刀'], ['剪刀', '布'], ['布', '石头']]
prompt = '''(0) 石头
(1) 剪刀
(2) 布
请选择(0/1/2): '''
pwin = 0  # 保存用户胜利的局数
cwin = 0  # 保存计算机胜利的局数

while pwin < 2 and cwin < 2:  # 人机都未赢2次，继续
    index = int(input(prompt))
    player = all_choices[index]
    computer = random.choice(all_choices)

    print('你选择了: %s, 计算机选择了: %s' % (player, computer))
    if player == computer:
        print('\033[32;1m平局\033[0m')
    elif [player, computer] in win_list:
        pwin += 1
        print('\033[31;1mYou WIN!!!\033[0m')
    else:
        cwin += 1
        print('\033[31;1mYou LOSE!!!\033[0m')
