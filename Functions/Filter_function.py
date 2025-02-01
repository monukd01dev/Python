people = {
    "Alice": 25,
    "Bob": 30,
    "Charlie": 22,
    "Diana": 28,
    "Ethan": 35,
    "Fiona": 27,
    "George": 24,
    "Hannah": 32,
    "Isaac": 29,
    "Julia": 26
}

# fiter out the person names below 25

result = filter(lambda _name,age:age<25 , people.items()) # iski bahen ke js acchi hai destructring ke mamle me #giving error lamda expecting two variable giving only one (name,age)
result = filter(lambda data:data[1]<25 , people.items()) # iski bahen ke js acchi hai destructring ke mamle me 

print(type(result),result)
myList = list(result)
print(myList)