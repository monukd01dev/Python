# there is not char data type shit in python only string which is an sequence of characters 
# and have indexing negative and positive both and strings are iterable in python

# and if it have indexing so we can access char at each index 
a = 'checking python indexing'

print(a[5])

#! we can only read it like this we cannot perform index based assignment in python on string casue strings are immutable 
# a[8] = 'jackma'
 # doesn't support item assignment //whill be the error

#! index out off range  
# print(a[100])

#! let's see forward and backward indexes in python 
print('--------indexing---------')
name = 'python'
      # 012345
rame = 'python'
      # -6-5-4-3-2-1 
      # why backward and negative indexing are reversing according to me minus ka number jinta chota unta bata tabhi -1 end index hai 

#! len() function return the count of elements in an iterable 
# print(len(rame)) #6
 
#! reversing of string using len()

for i in range(len(name) -1,-1,-1) :
    print(name[i],end="")




#in python slicing forward direction is increasing index 
print(name[3:1] +'\n') # is not valid cause index are decreasing and by default direction is forward left to right 
# give no error but print nothing
# cause there is not string exists in that range 
print(name[4:1:-1])


