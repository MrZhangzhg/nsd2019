from random import randint

def qsort(seq):
    '快速排序'
    # 序列长度小于2，不用排序，直接返回
    if len(seq) < 2:
        return seq

    # 假设第一个值是中间值，比它小的和大的各放到一个列表中
    m = seq[0]
    s = []
    l = []
    for data in seq[1:]:
        if data <= m:
            s.append(data)
        else:
            l.append(data)

    return qsort(s) + [m] + qsort(l)

if __name__ == '__main__':
    nums = [randint(1, 100) for i in range(10)]
    print(nums)
    print(qsort(nums))
