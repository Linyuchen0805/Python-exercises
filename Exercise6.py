##########Method 1###########

string = input("Say a string:")
a = len(string)
for i in range(0,a):
    if string[i]==string[a-i-1]:   #string[i]索引元素,string[i]==string[a-i-1]说明对称部分元素值相等
        if i < a-1:
            continue               #未遍历全部元素，需要继续进行循环
        elif i == a-1:             #遍历全部元素
            print("This string is a palindrome")
    else:
        print("This string is not a palindrome")
        break                      #有一个元素不符合，直接结束循环
		
##########Method 2###########

string = input("Say a string:")
reverse = string[::-1]           #将元素倒序
if string == reverse:
    print("This string is a palindrome")
else:
    print("This string is not a palindrome")
#[a:b]可以用来索引[a]到[b-1]的元素
#元素可以用倒序表示，如[1:-1]表示从第一个到倒数第二个
#[a:b:c]表示以c为间隔在[a:b]索引，c为正是正序，c为负是倒序