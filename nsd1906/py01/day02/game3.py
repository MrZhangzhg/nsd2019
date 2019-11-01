import random

all_choices = ['石头', '剪刀', '布']
win_list = [['石头', '剪刀'], ['剪刀', '布'], ['布', '石头']]
prompt = """(0) 石头
(1) 剪刀
(2) 布
请选择(0/1/2): """
computer = random.choice(all_choices)
ind = int(input(prompt))  # 将用户输入的数字字符转为数字
player = all_choices[ind]  # 将数字作为下标从列表中取出元素

print("Your choice: %s, computer's choice: %s" % (player, computer))
if player == computer:
    print('平局')
elif [player, computer] in win_list:
    print('You WIN!!!')
else:
    print('You LOSE!!!')
