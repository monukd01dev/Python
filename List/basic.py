'''
    1. Mutable -IMP
    2. Dinamically growable
    3. Index - IMP
    4. Order Preserve - IMP
    5. Slicing 
    6. Heterogenous Collection
    7. Dubplicate allowed -IMP
'''

# creating an List
l = [1,2,3,4,5]

print(l)

l = [*range(1,6)]
print(l)

#list constructor
l = list(range(1,11))
print(l)

#entering list from user input
l = eval(input("Enter Your List and please put the element inside the square braces : "))
print(type(l))

