a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []
for i in b:
    if i in a:
        c.append(i)
print(c)

###############################################

import random
a = [random.randint(1,100) for i in range(10)]
b = [random.randint(1,100) for i in range(10)]
c = []
for i in a:
    if i in b:
        c.append(i)
print(c)
#a = random.sample(range(100), 5) 另一种随机生成列表的方法