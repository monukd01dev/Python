# three type of string literals
a = 'hellow'
b = '''hellow'''
c = """hellow"""
d = "hellow"

if a==b==c==d :
    print("oky")
elif 1 :
    print('dash')
else :
    print('shit')

#indentation in python is everthing let me show you by using the multiple line string
#! so the below code give you error cause its not true 
# quote = "Each dog has a day 
# and you are an small elephant"

#! correct code using quote like string 
quote = '''one
two 
three
fours
 '''

print(quote)#even that will show you the \n means enter also

#! basically for multiline string we have tripple quote

#let me show you some escape sequencing \
someString = 'I want this string to be show in the single \'quote\''
print(someString)

# and that's how you done it