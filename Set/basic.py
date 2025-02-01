#
#! set basic is same as math sets cause it the same maths set
'''
    1. no duplicates
    2. no index
    3. no order
    4. no slicing
    5. heterogeneous
    6. mutable
    7. support comprehension
'''

#! stop sir, please understand this 
#* list -> []
#* tuple -> ()
#* dictionary -> {}
#* set -> set() #yes we create empty set like this in python

#! and set with elements like this 
s = {1}
print(s,type(s))
a = {'python'}
a1 = set('python')
# b = {[1,2,3,4,5,5,5,6,1,2,3]} #wrong syntax use constructed instead
b = set([1,2,3,4,5,5,5,6,1,2,3])
# c = {range(1,11)} #wrong syntax use constructor instead
c = set(range(1,11))
print(a,a1,b,c,sep=' | ')

#! add value in set
#* 1. adding single value using add() which will take only one element not list
#* meaning of add is what ever you give add inside the set as a single set element
a.add((1,2)) # I said list not tuple and string 
a.add('string')
# a.add([1,2,3,4,5])# give error says unhasable type well I have aready told you not pass list for list we have update()
print(a)

#* 2. adding multiple value using list using update(iterable) method
#* meaning of update is that add items from the iterable that we have passed 
#! update(iterable) take only iterables as argument
# a.update(4) # error not iterable
# print(a)

a.update('junk')
a.update(('ram','ram'))
a.update(['demaako','se','samajh','ko bachaoo'])
print(a)


#! removing element in set (using pop and remove)
#* always remember pop() return the deleted value and remove will return nothing in every context

#! pop()
'''
1. delete random element from set and return it
2. give error on empty set
'''

#! remove(value)
# give error is value is not found and no return

#! discard(value)
# no return and no error

#! refere chatGPT for set operational methods like 
'''
1. union() and  |
2. intersection() and &
3. difference() and -
4. symetric_difference and ^
'''

#! see comprehension in action
# a = { i for i in range(1,11) i%2==0} # wrong syntax
a = { i for i in range(1,11) if i%2==0}
print(a,type(a))