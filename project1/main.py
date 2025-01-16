import random

computer=random.choice([-1,0,1])
yourstr=input("Enter your choice: ")
youdict={"s":1,"w":-1,"g":0}
reverseDict={1:"snake",-1:"water",0:"gun"}
you =youdict[yourstr]
print(f"you chose {reverseDict[you]} \n computer chose {reverseDict[computer]}")
if(computer == you):
    print("It's a draw")

else:
    if(computer ==-1 and you ==1):
        print("you win")

    elif(computer ==-1 and you ==0):
        print("you lose")

    elif(computer ==1 and you ==-1):
        print("you lose")

    elif(computer ==1 and you ==0):
        print("you won")

    elif(computer ==0 and you ==-1):
        print("you won")

    elif(computer ==0 and you ==-1):
        print("you loose")   

    else:
        print("something went wrong")             


