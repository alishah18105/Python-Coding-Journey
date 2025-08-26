#Create a class programmer for storing information of few programmars working at Mlcrosoft

class Programmer:
    company = "Microsoft"

    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role
    
    def getInfo(self):
        print(f"The name of the programmer is {self.name}\n Salary is {self.salary}\n Role is {self.role}\n Company is {self.company}")
    
info = Programmer("Ali", 150000, "Developer")
info.getInfo()