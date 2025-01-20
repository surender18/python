# dunder method which is automatically called eg. __init__ is called automatically
# when an object is created
class empoyee:
    language="c"
    salary=1000

    def __init__(self,name,salary,language):
        self.name=name
        self.salary=salary
        self.language=language
        print("constructor is called")

    def getInfo(self):
        print(f"the language is {self.language} and the salary is {self.salary}")

jack=empoyee("jack",120000,"python")
jack.getInfo()
