from random import randint

def qsort(seq):
    if len(seq) < 2:
        return seq

    middle = seq[0]
    smaller = []
    larger = []

    for num in seq[1:]:
        if num <= middle:
            smaller.append(num)
        else:
            larger.append(num)

    return qsort(smaller) + [middle] + qsort(larger)

if __name__ == '__main__':
    nums = [randint(1, 100) for i in range(10)]
    print(nums)
    print(qsort(nums))
