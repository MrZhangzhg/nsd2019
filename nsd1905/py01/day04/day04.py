# import shutil
#
# shutil.copyfileobj()
# shutil.copyfile()
# shutil.copy()

from random import randint

nums = [randint(1, 100) for i in range(10)]
print(nums)

# for i in range(len(nums)):
#     print(i, nums[i])

print(list(enumerate(nums)))
for data in enumerate(nums):
    print(data)

for ind, num in enumerate(nums):
    print(ind, num)
