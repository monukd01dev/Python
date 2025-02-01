# Complex class to create a complex no 
# we have to undersant that complex number have two parts 
# a -> real part and bi = is the imaginary part
# so basically we need to parts means to instance variables 


'''
Understand the concept of operator overloading in python
so in python Object class is the top most class in python which have some magical method which have a naming convention 
it prefixed and suffixed with dunder like __add__() and this reperesent + operator in python

Now every thing in python is object 
so a+b where a and b are the object of class integer so basically there is nothing like primitive stuff is happening 
means that even for the int class + is overloaded 
we know that __add__() is defined in Object class and every class inherits Object class means int class also did it and now int class have the access to the magical method now it will write its own definition for __add__() or +
'''
class Complex : 
    '''complex class by KD'''

    #constructor
    def __init__(self,real=0,imag=0):
        self.__real = real
        self.__imag = imag
    
    @staticmethod
    def isComplex(comp)-> bool : 
        return isinstance(comp,Complex)
    
    def real(self):
        return self.__real
    
    def imag(self):
        return self.__imag
    
    def add(self,comp):
        if  not Complex.isComplex(comp) : 
            raise TypeError("Please provide a Complex number")
        else:
            return Complex((self.__real + comp.__real) , (self.__imag + comp.__imag))
        
    def sub(self,comp):
        if not Complex.isComplex(comp):
            raise TypeError("Please provide a Complex number")
        else:
            return Complex((self.__real - comp.__real) , (self.__imag - comp.__imag))
        
    
    def __add__(self,comp):
        if not Complex.isComplex(comp):
            raise TypeError("Please provide a Complex number")
        new_real = self.__real + comp.__real
        new_imag = self.__imag + comp.__imag
        new_comp = Complex(new_real,new_imag)
        return new_comp
    
    def __str__(self):
        return f"{self.__real} + {self.__imag}i"

c1 = Complex(2,3)
c2 = Complex(3,2)
try:
    c3 = c1 + c2
    print(c3)
except TypeError as e:
    print (e)

print(c3.__dict__)
try:
    c3 = c1.add(1)
    c3.display()
except TypeError as e:
    print (e)

