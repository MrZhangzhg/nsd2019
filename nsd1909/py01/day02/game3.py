import random

# 定义人胜利的情况
win_list = [['石头', '剪刀'], ['剪刀', '布'], ['布', '石头']]

# 计算机随机选择
xuanxiang = ['石头', '剪刀', '布']
computer = random.choice(xuanxiang)

# 获取用户的输入
prompt = '''(0) 石头
(1) 剪刀
(2) 布
请选择(0/1/2): '''
i = int(input(prompt))  # 将用户的输入转为数字
player = xuanxiang[i]   # 在列表中选择下标对应的字符串

# 输出人机的选择
print('您: %s, 计算机: %s' % (player, computer))

# 判断胜负
if player == computer:
    print('\033[32;1m平局\033[0m')
elif [player, computer] in win_list:
    print('\033[31;1mYou WIN!!!\033[0m')
else:
    print('\033[31;1mYou LOSE!!!\033[0m')

# echo -e "\033[31;43;1mOK\033[0m"
