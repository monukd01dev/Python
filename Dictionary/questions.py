#1. print the frequency of each character
'''
take input s.strip
loop over every character

'''

# s = "".join(input('Enter the string : ').strip().split())

# vowelonly = [i for i in s if i in ('a','i','e','o','u')] #my old way
vowelonly = [i for i in s if i in 'aeiouAEIOU'] # better way
print(vowelonly)
d ={}
dvo ={}
for char in s:
    d[char] = d.get(char,0) + 1
for char in vowelonly:
    dvo[char] = dvo.get(char,0) + 1

print(d,dvo)