marks=int(input("enter your marks:"))
if(marks<=100 and marks>=90):
    grade="O"
elif(marks<90 and marks>=80):
    grade="A"
elif(marks<50):
    grade="F"
print("Your grade is:",grade)            