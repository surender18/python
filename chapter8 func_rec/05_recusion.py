# factorial 
# n=n*fact(n-1)

def factorial(n):
    if(n==0 or n==1):
        return 1
    return n*factorial(n-1)

n=int(input("Enter number:"))
print(f"The factorial of {n} is :{factorial(n)}")
# needs to to base condition
