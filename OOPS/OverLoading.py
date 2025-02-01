#overloading

class Parent:
    def cruelty(self):
        print(self.__class__.__name__)

class Child(Parent):
    def cruelty(self):
        print(self.__class__.__name__)

ch1 = Child()
ch1.cruelty()