from random import randint

def qsort(seq):
    # 如果序列长度小于2，直接返回，不用排
    if len(seq) < 2:
        return seq

    # 假设第一项是中间值
    middle = seq[0]
    smaller = []  # 存放比中间值小的数字
    larger = []   # 存放比中间值大的数字

    # 遍历seq中剩余内容，比middle小的放到smaller中，大的放到larger中
    for data in seq[1:]:
        if data <= middle:
            smaller.append(data)
        else:
            larger.append(data)

    # 将三个部分拼接起来，smaller和larger用相同的方法继续排列
    return qsort(smaller) + [middle] + qsort(larger)

if __name__ == '__main__':
    nums = [randint(1, 100) for i in range(10)]
    print(nums)
    print(qsort(nums))
