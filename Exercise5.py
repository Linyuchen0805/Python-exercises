a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
list = []
for i in b:
    if i in a:
        list.append(i)
print(list)

################################################

import random                                       #导入random库
list1 = [random.randint(1,100) for i in range (10)] #随机生成1-100(包括1和100)内的10个整数
list2 = [random.randint(1,100) for i in range (10)]
list3 = []
for i in list1:
    if i in list2:
        list3.append(i)
print(list3)