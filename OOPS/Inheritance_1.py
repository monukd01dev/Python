#Inheritance in python on basic level basically in terms of calling the parent constructor is same as js but in python things in oops is more explicit than js 

# super().__init__() is necessary to ensure the parent’s constructor runs and initializes its attributes properly.
# Without calling super(), you can still access parent methods, but any attributes dependent on the parent’s constructor will not exist.
# It’s a good practice to always call super() unless you have a very specific reason not to.
# Python gives you flexibility, but with great power comes great responsibility! 😊

#super()__init__() isn't called automatically in python if you don't call it it will not be called 
#but still you can use the parent class method using Parent_name.method() but if this method using any attribute of parent class and which is not initialized for sure cause you haven't run the constructor so you will get an attribute error


class Vehical : 

    #constructor 
    def __init__(self,wheel):
        self.wheel = wheel
    
    #methods 
    #start
    def startEngine(self):
        print('Engine Started')
    
class Car(Vehical) : #bete yaha nhi hota hai extends yaha aise he hota hai 

    #constructor
    def __init__(self, wheel,brand):
        super().__init__(wheel)
        self.brand = brand

    
c1 = Car(4,'Tata')
c1.startEngine()