from functools import reduce

#! some of n natural number 

natural_number_sum = reduce(lambda x,y:x+y,[i for i in range(1,6)],1)
print(natural_number_sum)