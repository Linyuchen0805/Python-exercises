number = int(input("Say a number:"))

def prime(x):
    if x==1 or x==0:
        return 1
    for i in range(2,x):
        if x%i == 0:
            return 1
        else:
            if i < x-1:
                continue
            else:
                return 0
                break

if prime(number) == 1:
    print("Not prime")
elif prime(number) == 0:
    print("prime")