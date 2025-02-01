# The zip function combines two or more iterables (e.g., lists, tuples) element-wise into tuples. It returns a zip object (an iterator) containing these tuples.

numbers = [1,2,3,4]
num_word = ('one','two','three')
num_aplha_num = ['1_one',"2_two","3_three","4_four"]

zipped_num = zip(numbers,num_word,num_aplha_num) # retrun zip object an iterable 
print(list(zipped_num)) #ignores the '4_four' cause there is no pair for it

#! unzipping
#? this code have problem
# a,b,c = zip(*list(zipped_num))
# print(a,b,c)

# TODO : 
# What Happened?
# zip creates an iterator:

# The zip function returns a zip object, which is an iterator. Iterators can only be traversed once.
# First consumption with list(zipped_num):

# When you call list(zipped_num), the iterator is consumed to create a list. This means the data in zipped_num is exhausted and cannot be used again.
# Second attempt to unpack with zip(*list(zipped_num)):

# By the time you call zip(*list(zipped_num)), the zipped_num iterator is already empty. So, unzipping doesn't work because there is nothing left in the iterator.

zipped_list = zip(numbers,num_word,num_aplha_num)
my_list = list(zipped_list) # it consumed ones here and after this is cannot be iterated again
print(my_list)

a,b,c = zip(*my_list)
print(a,b,c)

'''
Why Does It Ignore '4_four'?
The zip function stops creating tuples as soon as the shortest iterable is exhausted. In this case:

numbers has 4 elements.
num_word has 3 elements.
num_aplha_num has 4 elements.
Since num_word is the shortest iterable, zip stops at its length (3). So, '4_four' and 4 are ignored because there is no corresponding element in num_word.

Key Takeaways
Zip objects are iterators and can only be consumed once.
If you need to use the zipped data multiple times, store it in a list.
The zip function stops when the shortest input iterable is exhausted.
'''
