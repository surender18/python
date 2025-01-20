# instance attribute are preffered over class attribute during assignment and retrievalclass student:
class student:
   
    std="VI"
    roll="56"

jacky=student() 
jacky.std="VII"
print(jacky.roll,jacky.std)