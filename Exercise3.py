a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for i in a:
    if i <5:
        print(i)

#Add these valuse into a new list
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
for i in a:
    if i <5:
        b.append(i)
print(b)

###########################################

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#b = [i for i in a and i <5]#错误例子,不能用and
b = [i for i in a if i <5]  #将上述代码写在一行里
print(b)

###########################################

number = int(input("say a number"))
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
for i in a:
    if i < number:
        b.append(i)
print(b)
        