from random import randint

def qsort(seq):
    if len(seq) < 2:
        return seq

    # 假设第1个数是中间值
    middle = seq[0]
    smaller = []
    larger = []

    # 遍历后续数字，比中间值小的放到smaller，大的放到larger
    for data in seq[1:]:
        if data <= middle:
            smaller.append(data)
        else:
            larger.append(data)

    # 把三项数据拼接，smaller和larger采用相同的方法继续排序
    return qsort(smaller) + [middle] + qsort(larger)

if __name__ == '__main__':
    nums = [randint(1, 100) for i in range(10)]
    print(nums)
    print(qsort(nums))
