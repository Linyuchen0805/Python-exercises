name1 = input("What is your name?")
a = input("Rock Paper Scissors?")
name2 = input("What is your name?")
b = input("Rock Paper Scissors?")

def gamewinner(x,y):
    if x == "Rock":
        if y == 'Scissors':
            return name1
        elif y == 'Rock':
            return 0
        else:
            return name2
    elif x == 'Scissors':
        if y == 'Rock':
            return name2
        elif y == 'Scissors':
            return 0
        else:
            return name1
    else:
        if y == 'Rock':
            return name1
        elif y == 'Paper':
            return 0
        else:
            return name2 
print(gamewinner(a,b))
answer = input("Congratulations,Want to start a new game?")

while answer=='Yes':
    name1 = input("What is your name?")
    a = input("Rock Paper Scissors?")
    name2 = input("What is your name?")
    b = input("Rock Paper Scissors?")
    if gamewinner(a,b)!=0:
        print(gamewinner(a,b))
        answer = input("Congratulations,Want to start a new game?")
    else:
        print("Equal")
        break