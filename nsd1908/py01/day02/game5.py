import random

choices = ['石头', '剪刀', '布']
# 将人胜利的情况，提前定义到列表中，人在前，计算机在后
win_list = [['石头', '剪刀'], ['剪刀', '布'], ['布', '石头']]
prompt = """(0) 石头
(1) 剪刀
(2) 布
请选择(0/1/2): """
cwin = 0
pwin = 0

while 1:
    computer = random.choice(choices)
    ind = int(input(prompt))
    player = choices[ind]

    print("Your choice: %s, Computer's Choice: %s" % (player, computer))
    if player == computer:
        print('\033[32;1m平局\033[0m')
    elif [player, computer] in win_list:  # 人机选项的小列表是大列表的一项
        pwin += 1
        print('\033[31;1mYou WIN!!!\033[0m')
    else:
        cwin += 1
        print('\033[31;1mYou LOSE!!!\033[0m')

    if pwin == 2 or cwin == 2:
        break
