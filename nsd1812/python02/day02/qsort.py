from random import randint

def qsort(seq):
    if len(seq) < 2:  # 如果长度小于2，不用排序，直接返回
        return seq

    middle = seq[0]   # 假定第一个数是中间值
    smaller = []      # 用于保存比中间值小的数据
    larger = []       # 用于保存比中间值大的数据

    for i in seq[1:]:
        if i < middle:
            smaller.append(i)
        else:
            larger.append(i)

    # 注意middle不是列表，需要把它放到列表中
    return qsort(smaller) + [middle] + qsort(larger)

if __name__ == '__main__':
    nums = [randint(1, 100) for i in range(10)]
    print(nums)
    print(qsort(nums))
