# The default mutable arguments pitfall in Python arises when a mutable object (like a list or dictionary) is used as a default argument in a function. This can lead to unexpected behavior because default argument values are evaluated once when the function is defined, not each time the function is called.

def append_val (value,myList=[]) :# this default argument value evaluated only once when function is defined not each time function is called
    myList.append(value)
    return myList

print(append_val(1))
print(append_val(2))

#! How to Avoid This Pitfall
#? The best practice is to use None as the default argument and initialize the mutable object inside the function:

def append_val(value,myList=None) :
    if myList is None:
        myList =[]
    myList.append(value)
    return myList

print(append_val(2))
print(append_val(4))
print(append_val(100))

