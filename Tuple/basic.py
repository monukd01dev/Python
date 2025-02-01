#
#! in python there is no concept of constants
#? you want to constant you can use tuple 

#* What is tuple 
'''
    1. same as list but it is an immutable list 
        a. ones created you cannot change any element from it 
    2. Have indexing 
    3. Have order
    4. Have slicing 
    5. No comprehension
    6. Heterogeneous 
    7. Have Duplicate 
'''

#! lets see the creation of tuples 
#? as we already knew that lists are created using [] 
    #* for tuple we use ()

#! creation of an empty tuple
t = ()
print(type(t))

#! creating a tuple with only one element 
t = (1)
print(type(t)) #* output : <class 'int'>

#? if (1) this is considered as tuple then what would you think this (2**2)/4 would be, that's why we cannot create a tuple with single value like this 
#? that would be considered as int 

#? creating of single value tuple and how constant/readOnly data is created in python 
t = (1,) #! we just have to put an comma at the end to make it tuple 
print(type(t))

#but can't you see that there is no use of it cause what constant mean is totaly different and immutability is totaly different 
# the concept of constant is for the variable/identifiers not for the value

#! creating of tuple using packing
t = 1,2,3 #it will be treated as (1,2,3) packing happening here
t = 1, 
print('t=1, is also : ',type(t))

#! sorting of tuple using sort() method
# recall what sort method do sort() method will mutate the list but can tuple is mutalbe off course not so how we use sort() over it
# and sort is method of list class and it is not available for tuple
#* for tuple we use an generalize method called sorted()
    #* which will not mutate the actual collection but return the sorted one 
t = (5,8,1,7,6,9)
print(sorted(t,reverse=True))
print(sorted(t))

#! + concate and * repetion opertor on tuple 
#? they are not modify the actual tuple but return the result 
y = t + ('some','things','inside')
print(y)
print(type(y))

#? contact work with every data type if both the operand have the same type

z = 1,2,1
print(z*3)

#! min() and max() function on tuple
print(max(t),min(t))

#! so you already know packing lets see `unpacking` work as destructuring in js
#so we knew that z have 3 elements 1,2,1
a,b,c = z
# now a=1,b=2,c=1 this is called unpacking
# but LHS must be equal to RHS not have features like js destruing #! no it have those features also


# *unpacking with `*`
a, *b = t
print(a,type(a))
print(b,type(b)) # will get a list

#! _ is widely used as a placeholder, for ignoring values, or for special conventions in programming.
# underscore ki mahima samjhe

#from a tuple I need only first value not any of it 
a=z# this will perform alias
# a,b = z # this will give error 
print(a)

#* for doing this we have two ways 
#? 1. slicing/indexing

a = z[0]
print(a)

#? 2. Using Unpacking with a `_` Throwaway Variable

a,*_ =z
print(a,type(a))

# Here:
# a gets the first value (1).
# *_ ignores the rest of the list.

#! let's see they have skiping or not 
# 1. Using a Throwaway Variable (_) to Skip Values
# You can use _ as a placeholder to explicitly ignore elements while unpacking:

a, _, b, _, _, c = (1, 2, 3, 5, 4, 6)
print(a)  # Output: 1
print(b)  # Output: 3
print(c)  # Output: 6

