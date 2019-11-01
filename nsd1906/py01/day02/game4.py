import random

all_choices = ['石头', '剪刀', '布']
win_list = [['石头', '剪刀'], ['剪刀', '布'], ['布', '石头']]
prompt = """(0) 石头
(1) 剪刀
(2) 布
请选择(0/1/2): """
pwin = 0  # 人的计分板
cwin = 0  # 计算机的计分板

while pwin < 2 and cwin < 2:
    # 人和计算机都没有赢够两次则继续
    computer = random.choice(all_choices)
    ind = int(input(prompt))  # 将用户输入的数字字符转为数字
    player = all_choices[ind]  # 将数字作为下标从列表中取出元素

    print("Your choice: %s, computer's choice: %s" % (player, computer))
    if player == computer:
        print('\033[32;1m平局\033[0m')
    elif [player, computer] in win_list:
        pwin += 1  # 人赢的时候，计算器加1
        print('\033[31;1mYou WIN!!!\033[0m')
    else:
        cwin += 1
        print('\033[31;1mYou LOSE!!!\033[0m')
