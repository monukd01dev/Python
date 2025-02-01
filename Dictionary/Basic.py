# <class 'dict'>
d = {}
print(type(d))

#! key is always unique but values will be duplicate

#! creation of dictionary
'''
1. single (key, value) adding 
2. giving pair of key values
3. givin only keys 
4. giving only keys with specified default value
'''
#! getting values in form of list 
d = {1:'one',2 : 'two',3:'three',4: 'four'}
print(d.values(),type(d.values())) 
print(d.keys(),type(d.keys()))
print(d.items(),type(d.items()))
print(len(d))

#! updation of value 
'''
1. dict_ref[key] = new_value
2. updating with another dictionary 
    a. a.update(b) a = a+b
'''

#! deleting and removing and clearing 
'''
1. del 
    a. del entire_dict
    b. del dict_ref[key] 
    c. both give error

2. dict_ref.pop(key)
    a. delete pair and return in value only
3. dict_ref.popitem()
    a. random pair deletion and return pair and error on empty dict
4. dict_ref.clear() => {}

'''
