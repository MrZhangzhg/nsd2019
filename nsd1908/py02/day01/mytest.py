import get_info

name = '牛老师'
age = 20
age2 = 200

try:
    get_info.get_info(name, age)
    get_info.get_info2(name, age2)
except (ValueError, AssertionError) as e:
    print('Error:', e)


