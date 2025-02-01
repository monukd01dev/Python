# ! 1. wrtie a program to print the even length words only from string 
s = "Dekh karni hai jo sirf even ho aur baaki bache to ood he honge na"

word_list = s.split()

for word in word_list : 
    if len(word)%2 == 0 :
        print(word,end=' ')

# ! 2. WAP to print the first character of even length words from the string whole word if length is odd

print("")
for word in s.split():
    print(word[0],end=" ") if len(word)%2 ==0 else print(word,end=" ") 

# ! 3. only print the last word complete in a string 
print("")
'''
    1. split to get the word list 
    2. on the basis of condition print the last word complete
'''

for i,word in enumerate(s.split()):
    print(word,end=' ') if len(s.split())-1==i else print(word[0],end=" ")

#? another implementation
print("")
updated_list = []

for word in word_list[:len(word_list)-1] : #slicing list me bhi ho sakti hai kyonki index to vaha bhi hai
    updated_list.append(word[0])

updated_list.append(word_list[len(word_list)-1])

#now updated_list is an list not string
print(updated_list)

print(" ".join(updated_list))



#! 4. Let's replacing the first and last word of an string 
print("")
'''
    1. slice the string 
    2. append first word and prepend the lastword
    3. join the sliced string
'''

s = "Python is not Java"

sliced_list = s.split()[1:len(s.split())-1]
sliced_list.insert(0,s.split()[len(s.split())-1])
sliced_list.append(s.split()[0])

print(" ".join(sliced_list))

#? jaadu

s = input("Enter your String : ");
print(' '.join(s.split()[::-1]));


#! 5 Reverse all the word in an string
'''
    1. collect the splited wordlist
    2. create an empty list 
    3. iterate over the splited word one by one
    4. reverse the word ans appen in the empty list
    5. join the empty list

'''

emptyList = []

for word in s.split() : 
    emptyList.append(word[::-1])
print(" ".join(emptyList))