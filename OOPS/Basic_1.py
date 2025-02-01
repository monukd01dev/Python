class Employee : 
    # static Variable 
    employeeCount = 0

    def __init__(self,name,age):
        self.name = name
        self.age = age
        Employee.employeeCount+=1
         
    
    def __str__(self):
        return f'EmployeeCount : {Employee.employeeCount} | Name : {self.name} | Age : {self.age}'
    
e1 = Employee('Ajay',25)
print(e1)
e2 = Employee('Vijay',30)
e2.employeeCount = 0 # when you change the employeeCount using the object reference then the static variable value is updated for that specific object is 0 
# means for e2 we have employeeCount = 0 
# but every other object it is what it is 
# so only use static varaible with the class name and cls
print(e2.employeeCount)
print(e2) # this is printing employeeCount 2 cause in __str__ method you have printed the employeeCount using the Employee 

#You can modify a static variable via an object, but this creates a new instance attribute for that specific object, leaving the class's static variable unchanged.
print(e1.__dict__)
print(e2.__dict__) # as you can see in the output that an new instance variable is created for the e2 only 
