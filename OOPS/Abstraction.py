# ABC module and @abstractmethod decorator
# to be an abstract class at least one @abstractmethod is required otherwise your class is can be instanciated 

from abc import ABC,abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

    @abstractmethod
    def move(self):
        pass

class Dog(Animal):
    # pass

    def sound(self):
        print('bark!!')

    def move(self):
        pass

d1 = Dog()
d1.sound()