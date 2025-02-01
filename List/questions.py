    # #
    # #! Input taking 
    #     # input = 1 2 3 4 5
    #     # output = [1,2,3,4,5]

    # s = input("Enter you list elements separated by space : ")
    # s = s.split()

    # l = []
    # for num in s :
    #     l.append(int(num))

    # print(l)

    # #! Until n 

    # n = int(input('Enter the value of n : '))
    # l= list(range(1,n+1))
    # print(l)

#! looping the input 
# l = []
# # n = int(input())
# for i in range(int(input())) :
#              l.append(int(input()))
# print(l)

#! List comprehension in python

#? basic example 
print([i for i in range(5)])

#? creating an 2d multiplication tabel
'''
    [
        [1,2,3,4,5],
        [2,4,6,8,10],
        [3,6,9,12,15],
        [5,10,15,20,25]
    ]
'''

n = int(input('Enter the number upto 10 : '))

table = [
    [i*x for i in range(1,n+1)] for x in range(1,n+1)
]
print(table)

#! flatten a List like table 
flatten_table = [item for subList in table for item in subList]
print(flatten_table)

#! checking loop 
print([(a,b,c) for a in range(1,5) for b in range(a,5) for c in range(b,5)])
print(len([(a,b,c) for a in range(1,5) for b in range(a,5) for c in range(b,5)]))
print([(a,b,c) for a in range(1,20) for b in range(a,20) for c in range(b,20) if a**2 + b**2 == c**2])