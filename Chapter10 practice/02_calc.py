class calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def add(self):
        print(f"the sum of {self.a} and {self.b} is {self.a+self.b}")

a=calculator(5,4)
a.add()
