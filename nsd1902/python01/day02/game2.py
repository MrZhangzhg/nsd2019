import random

all_choices = ['石头', '剪刀', '布']
win_list = [['石头', '剪刀'], ['剪刀', '布'], ['布', '石头']]
computer = random.choice(all_choices)
player = input('石头/剪刀/布: ')

print("Your choice: %s, Computer's choice: %s" % (player, computer))
if player == computer:
    print('\033[32;1m平局\033[0m')
elif [player, computer] in win_list:
    print('\033[31;1mYou Win!!!\033[0m')
else:
    print('\033[31;1mYou Lose!!!\033[0m')
