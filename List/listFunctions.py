#
#! append() 
'''
 1. add at end
 2. only take one argument of any type
 3. raise error for more than one argument
 4. modify the original list cause list in mutable
 5. return none
'''
l = [12,23,45]
l.append([11,22,33,44])
# l.append(*[11,22,33,44]) #TypeError: list.append() takes exactly one argument (4 given)
print(l)

#! insert(index,value)
'''
    1. Insert element at specified index
    2. Add only one element at a time
    3. return none
    4. modify
    5. +ve index out of rande add at end -ve index out of range add at start
'''
print(l.insert(100,3))

#! extend(iterable)
'''
    1. Extends the list by appending elements from an iterable.
    2. Adds multiple elements at once (from the iterable).
    3. Returns None.
    4. Modifies the original list.
    5. Raises a TypeError if the argument is not iterable.
    6. Strings are treated as iterables and are unpacked into individual characters.
    #?7. only take one iterable at a time 
'''

l.extend(['sita','sita-ram'])
l.extend('monukd')
print(l)

k = [*'jack']
k.extend('jack')
print(k)


#! Delete Operation functions on List
#* remove(value)
'''
 1. remove 
 2. return nothing
 3. give error is element not present
 4. modify
'''
print(l.remove(3))# none
# l.remove(3)# error

# oky
if 3 in l : 
    l.remove(3)

#* pop() and pop(value)
#* pop(index=-1)
'''
    1. Removes and returns the element at the specified index.
    2. Default index is -1 (last element).
    3. Modifies the original list.
    4. Returns the removed element.
    5. Raises an IndexError if the list is empty or if the index is out of range.
    6. Supports both positive and negative indexing.
'''
# z = []
# z.pop()#error : pop for empty list

z = [1,2,3,4,5]
z.pop()
print(z)
z.pop(0)
print(z)

#! searching and sorting in list 
#* index(value, start=0, end=len(list))
'''
    1. Returns the first index of the specified value in the list.
    2. Searches between optional start and end parameters (inclusive of start, exclusive of end).
    3. Raises a ValueError if the value is not found.
    4. Supports both positive and negative indexing.
    5. Does not modify the original list.
'''
print(z.index(2))


#* sort(key=None, reverse=False)
'''
    1. Sorts the elements of the list in place in ascending order by default.
    2. Modifies the original list.
    3. Returns None.
    4. Can use the optional `key` parameter to specify a custom sorting function.
    5. The optional `reverse` parameter can be set to True for descending order.
    6. Raises a TypeError if the elements are not comparable (e.g., mixing strings and numbers).
'''
people = [("Alice", 25), ("Bob", 20), ("Charlie", 30), ("Diana", 22)]
people.sort(key= lambda people: people[1])# understand lamda as arrow function people => people[1]
print(people)

words = ["apple", "kiwi", "banana", "grape", "cherry"]
words.sort(key= lambda word: (len(word),word))

print(words)

numbers = [5, 1, 10, 7, 3]
target = 6
numbers.sort(key= lambda num: abs(target-num))# convert nagative to positive abs
print(numbers)
#* reverse()
'''
    1. Reverses the elements of the list in place.
    2. Modifies the original list.
    3. Returns None.
    4. Does not create a new list.
    5. Works with lists of any comparable elements but does not sort.
'''
