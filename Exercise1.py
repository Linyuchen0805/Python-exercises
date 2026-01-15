name = input("What is you your name?")
age = int(input("What is your age?"))  #input()只能获得string值，如果要转化成整数需要用到int(input())
year = 100-age+2026
print(name,"You will be 100 in",year)