import random

win_list = [['石头', '剪刀'], ['剪刀', '布'], ['布', '石头']]
xuanxiang = ['石头', '剪刀', '布']
prompt = '''(0) 石头
(1) 剪刀
(2) 布
请选择(0/1/2): '''
pwin = 0  # 定义人胜利的计数器
cwin = 0  # 定义计算机胜利的计数器

while 1:  # 1是非0值，表示True，也就是条件永远为真
    computer = random.choice(xuanxiang)
    i = int(input(prompt))  # 将用户的输入转为数字
    player = xuanxiang[i]   # 在列表中选择下标对应的字符串
    # 输出人机的选择
    print('您: %s, 计算机: %s' % (player, computer))

    # 判断胜负
    if player == computer:
        print('\033[32;1m平局\033[0m')
    elif [player, computer] in win_list:
        print('\033[31;1mYou WIN!!!\033[0m')
        pwin += 1
    else:
        print('\033[31;1mYou LOSE!!!\033[0m')
        cwin += 1

    if pwin == 2 or cwin == 2:
        break
