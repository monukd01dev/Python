#map function in python 
# higher Order function
# arguments 2 -> 1.function and 2.Iterable

'''
# Function to square a number
def square(x):
    return x * x

# Use map to apply the function to each element in a list
numbers = [1, 2, 3, 4, 5]
squared_numbers = map(square, numbers)

print(list(squared_numbers))  # Output: [1, 4, 9, 16, 25]

'''

squared_Numbers = map(lambda x : x*x,[i for i in range(1,11)])
print(squared_Numbers) # we have to convert it into list
print(list(squared_Numbers))