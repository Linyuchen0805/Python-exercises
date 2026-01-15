number = int(input("How many Fibonacci numbers to generate?"))

def Fibonacci(iteration):
    if iteration ==1:
        return[1]
    elif iteration ==2:
        return[1,1]
    else:
        list =[1,1]
        for i in range(2,iteration):
            add = list[i-1]+list[i-2]
            list.append(add)
        return list
print("The result is:",Fibonacci(number))