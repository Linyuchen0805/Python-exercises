number = int(input("Say a number"))
list = []
for i in range(2,number+1):  #range()函数算头不算尾
    if number%i == 0:
        list.append(i)
print(list)