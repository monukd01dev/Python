'''
    Key Concepts:
Private Variables (__variable):

    Yeh variables directly access nahi kar sakte outside the class. Python internally name mangling use karta hai, jisme private variables ka naam thoda change ho jata hai to avoid direct access.
    Example: __salary ko self._Person__salary ke naam se access kar sakte ho, but yeh best practice nahi hai.
Protected Variables (_variable):

    Yeh variables subclasses ke through access kiye ja sakte hain, but outside the class direct access nahi karna chahiye.
    Public Variables (variable):

    Yeh directly access kiye ja sakte hain.
Getter and Setter Methods:

Getter: Yeh method variables ko access karne ka controlled tarika deta hai.
Setter: Yeh method variables ko set karne ka controlled tarika deta hai, jisme aap kuch conditions apply kar sakte ho.
@property decorator is used to create getter methods, aur setter ke liye @<property_name>.setter decorator use hota hai.
'''

'''
The error in your code happens because you are using @salary.setter without defining a getter method first. In Python, the getter method must exist before you can define the setter method for a property.
'''

class Person:

    def __init__(self,name,age,salary):
        self.name = name
        self._age = age
        self.__salary = salary

    #getter hai ye
    @property 
    def salary(self):
        return self.__salary
    

    @salary.setter
    def salary(self,value):
        self.__salary = value


p1 = Person('ajay',39,'10LPA')

print(p1._Person__salary) #security breach when you put __ to pake private what does it do behind the scene it change the variable name to _className__property_name basically prefix with _className and when you try to access like below you get the error
'''
Agar tum __salary ko directly access karne ki koshish karoge toh wo name mangling ke wajah se access nahi kar paoge:'''
# print(p1.__salary) # no attribute exists


# now see for protected
print(p1._age) #easy accessible without any warning 

# python be like please follow the convention
# Java be like what do you mean by request it's an order KID