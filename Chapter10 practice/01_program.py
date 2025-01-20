# class programmer:
#     name="jack"
#     language="c"
#     salary=100000
#     company="microsoft"

#     def getInfo(self):
#         print(f"name of programmer is {self.name} ,the language selected by programmer is {self.language} and the salary of programmer is {self.salary} working at {self.company}")

# jack=programmer()
# jack.getInfo()


class programmer:
    company="microsoft"
    def __init__(self,name,salary,language):
        self.name=name
        self.salary=salary
        self.language=language

sk=programmer("jack",120000,"python")
print(sk.name,sk.salary,sk.language)        
r=programmer("rohan",1200000,"python")
print(r.name,r.salary,r.language)        
