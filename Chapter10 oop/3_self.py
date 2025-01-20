class student:
   
    std="VI"
    roll="56"

    def getInfo(self):
        print(f"the std is {self.std} and the roll is {self.roll}")

jacky=student() 
jacky.std="VII"
jacky.getInfo()
# student.getInfo(jacky)
