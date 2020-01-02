import random

choices = ['石头', '剪刀', '布']
computer = random.choice(choices)
player = input('请出拳(石头/剪刀/布): ')

print("Your choice: %s, Computer's Choice: %s" % (player, computer))
if player == '石头':
    if computer == '石头':
        print('\033[32;1m平局\033[0m')
    elif computer == '剪刀':
        print('\033[31;1mYou WIN!!!\033[0m')
    else:
        print('\033[31;1mYou LOSE!!!\033[0m')
elif player == '剪刀':
    if computer == '石头':
        print('\033[31;1mYou LOSE!!!\033[0m')
    elif computer == '剪刀':
        print('\033[32;1m平局\033[0m')
    else:
        print('\033[31;1mYou WIN!!!\033[0m')
else:
    if computer == '石头':
        print('\033[31;1mYou WIN!!!\033[0m')
    elif computer == '剪刀':
        print('\033[31;1mYou LOSE!!!\033[0m')
    else:
        print('\033[32;1m平局\033[0m')
