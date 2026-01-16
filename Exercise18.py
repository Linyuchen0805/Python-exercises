number = input("Say a 4-digit number:")
list_answer = [random.randint(1,9) for i in range(4)]
list_number = [int(i) for i in number]
print(list_number)
print(list_answer)
guesstime =1
while list_number != list_answer:
    a=0
    b=0
    guesstime+=1
    for i in range(0,4):
        if list_number[i]==list_answer[i]:
            a+=1
            continue
        else:
            if list_number[i] in list_answer:
                b+=1
                continue
            else:
                continue
    print(f"{a} cow,{b} bull")
    list_number = [int(i) for i in input("Say a 4-digit number:")]

print("Game is over,total time is:",guesstime)
#当列表中存在重复元素时，用index索引重复元素的位置，只能得到最靠前的位置，因为列表索引是默认从左到右的