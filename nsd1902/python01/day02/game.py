import random

all_choices = ['石头', '剪刀', '布']
computer = random.choice(all_choices)
player = input('石头/剪刀/布: ')

print("Your choice: %s, Computer's choice: %s" % (player, computer))
if player == '石头':
    if computer == '石头':
        print('平局')
    elif computer == '剪刀':
        print('You Win!!!')
    else:
        print('You Lose!!!')
elif player == '剪刀':
    if computer == '石头':
        print('You Lose!!!')
    elif computer == '剪刀':
        print('平局')
    else:
        print('You Win!!!')
else:
    if computer == '石头':
        print('You Win!!!')
    elif computer == '剪刀':
        print('You Lose!!!')
    else:
        print('平局')
