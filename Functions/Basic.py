def name (game) :
 return f'name ka game {game}'

game = lambda game : f'game ka name {game}'

'''
Types of Arguments:

    1. Positional Arguments: Passed in order.
    2. Keyword Arguments: Passed with a name.
    3. Default Arguments: Have default values.
    4. Variable-Length Arguments: Use *args and **kwargs.

'''
# ! 1. positional argument
def jama(a,b) : 
    return a+b

print(jama(1,2))# positional a->1 and b->2

def jama(a,b,c):
    return a+b+c

# print(jama(1,23))#erro : one argument is missing


# ! 2. keyword argument # order doesn't matter init

def jama(a,b,c,d):
   return a+b+c+d

print(jama(d=4,a=1,b=2,c=3))
# and if you want to mix positional and keyword argument you have put the postional arguments first then keyword 
print(jama(1,2,d=4,c=5)) # common sense

#! 3. default arguments 
def pow(a=1,b=1):
   return a**b

print(pow(2,4))# 4 override the fault value 
print(pow(2)) # b uses the default value cause no value is passed for the b 

#! Variable length arguments

def jamaall(*args):
    print(type(args))
    return sum(args)

print(jamaall(1,2,3,4))

#! keyword variable length args
def makePiar(**kwargs):
    print(type(kwargs))
    for k,v in kwargs.items():
       print(f'key : {k} | Value : {v}')


makePiar(fname='Monu',lname='KD',email='monukd01dev@gmail.com',membership='premium')

