from random import randint

def qsort(seq):
    # 如果对象的长度是0或1，那么直接返回，不用再排序
    if len(seq) < 2:
        return seq
    # 假设第一个数是中间值，比它小的放到一个列表
    # 比它大的放到另一个列表
    middle = seq[0]
    smaller = []
    larger = []
    for i in seq[1:]:
        if i <= middle:
            smaller.append(i)
        else:
            larger.append(i)

    # 把各项从小到大拼接。如果对列表继续进行排序
    return qsort(smaller) + [middle] + qsort(larger)


if __name__ == '__main__':
    nums = [randint(1, 100) for i in range(10)]
    print(nums)
    print(qsort(nums))
