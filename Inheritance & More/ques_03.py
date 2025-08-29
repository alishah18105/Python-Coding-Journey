#Create a class "Employee" and add a salay and increment properties to it.
#Write a method "salary_after_increment" with a @property decorator with a setter which changes the value of increment
#based on salary

class Employee:
    def __init__(self,salary, increment):
        self.salary = salary
        self.increment = increment
    
    @property
    def salary_after_increment(self):
        return f"Your Salary After Increment Is: {self.salary + (self.salary * self.increment)/100}"
    
    @salary_after_increment.setter
    def salary_after_increment(self, increment):
        self.increment = (increment * self.salary)/100


e = Employee(50000,10)
print(e.salary_after_increment)
e.salary_after_increment = 10
print(e.increment)