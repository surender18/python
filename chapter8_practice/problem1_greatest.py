'''
a=2
b=3
c=8
def great():
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>a and c>b):
        return c
    else:
        print("invalid input")
    print(great)
    
great()    
'''


def greatest(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>a and c>b):
        return c
    else:
        print("invalid input")


a=2
b=3
c=8 

# result=greatest(a,b,c)
# print("The greatest no is:",result)
print(greatest(a,b,c))