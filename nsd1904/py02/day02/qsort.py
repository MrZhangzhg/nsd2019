from random import randint


def qsort(seq):
    """
    如果序列长度是0或1，则直接返回。
    假设序列中的第一个数为中间值，比它大的放到大列表，比它小的放到小列表。
    最后再对两个列表通过同样的方法继续排序。
    """
    if len(seq) < 2:
        return seq

    middle = seq[0]
    larger = []
    smaller = []

    for i in seq[1:]:
        if i > middle:
            larger.append(i)
        else:
            smaller.append(i)

    return qsort(smaller) + [middle] + qsort(larger)


if __name__ == '__main__':
    nums = [randint(1, 100) for i in range(10)]
    print(nums)
    print(qsort(nums))
