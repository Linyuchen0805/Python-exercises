number = int(input("say a number"))
if number!=0:
    if number%2==0:
        if number%4==0:
            print("multiple of 4")
        else:
            print("even")
    else:
        print("odd")
else:
    print("not even or odd")
    
############## Extra ################

num = int(input("say a number:"))
check = int(input("say another number:"))
if num%check==0:
    print("Check divides evenly into num")
else:
    print("Check not divides evenly into num")