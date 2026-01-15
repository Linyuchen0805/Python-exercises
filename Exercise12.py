import random
def firstandlast(a):
    return [a[0],a[-1]]
list1 = [random.randint(1,100) for i in range(10)]
print(firstandlast(list1))