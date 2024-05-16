import random

game=["stone","paper","scissor"]
userPoint=0
userPoint=int(userPoint)
compPoint=0
compPoint=int(compPoint)

while (1):
    print("Choose stone ,paper or scissor")
    user=input()
    comp=random.choice(game)
    print("Computer's choice",comp,"your choice",user)
    if user=="stone" and comp=="stone":
        print("tie")
    elif user=="stone" and comp=="paper":
        print("computer wins")
        compPoint+=1
    elif user=="stone" and comp=="scissor":
        print("you won")
        userPoint+=1
    elif user=="scissor" and comp=="scissor":
        print("tie")
    elif user=="scissor" and comp=="stone":
        print("computer wins")
        compPoint+=1
    elif user=="scissor" and comp=="paper":
        print("you won")
        userPoint+=1
    elif user=="paper" and comp=="paper":
        print("tie")
    elif user=="paper" and comp=="stone":
        print("you won")
        userPoint+=1
    elif user=="paper" and comp=="scissor":
        print("computer wins")
        compPoint+=1
    if userPoint==5 or compPoint==5:
        break
print("your score",userPoint,"Computer score",compPoint,sep="\n")
if userPoint<compPoint:
    print("computer won")
else:
    print("You won")

    
