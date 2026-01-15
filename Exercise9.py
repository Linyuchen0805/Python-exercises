import random
number = input("Say a number")
answer = random.randint(1,9)
time=0

while number!= 'Exit':
    if int(number)==answer:
        print("Exactly right")
        time+=1
        break
    else:
        if int(number)>answer:
            print("Too high")
        else:
            print("Too low")
        time+=1
    number = input("Say a number")
print("Total time:",time)