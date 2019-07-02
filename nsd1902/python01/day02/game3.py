import random

all_choices = ['石头', '剪刀', '布']
win_list = [['石头', '剪刀'], ['剪刀', '布'], ['布', '石头']]
prompt = """(0) 石头
(1) 剪刀
(2) 布
请选择(0/1/2): """

computer = random.choice(all_choices)
ind = int(input(prompt))   # prompt就是上面的4行文件，作为屏幕提示语
player = all_choices[ind]  # 在列表中取出下标对应的字符串

print("Your choice: %s, Computer's choice: %s" % (player, computer))
if player == computer:
    print('\033[32;1m平局\033[0m')
elif [player, computer] in win_list:
    print('\033[31;1mYou Win!!!\033[0m')
else:
    print('\033[31;1mYou Lose!!!\033[0m')
