n=int(input("Enter no "))
 
for i in range(2,n):
    if(n%i) == 0:
        print("No  is not prime")
        break
else:
    print("Number is prime")    