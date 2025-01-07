mark1=int(input("enter subject 1 marks"))
mark2=int(input("enter subject 2 marks"))
mark3=int(input("enter subject 3 marks"))

total_percentage=100*(mark1+mark2+mark3)/300
if(total_percentage>=40 and mark1>33 and mark2>33 and mark3>33):
    print("you are passed:",total_percentage)

else:
    print("you are failed",total_percentage)    

