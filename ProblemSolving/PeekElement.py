# find the peek element from the given list
# l = [1,3,2,5,8,10,7]
# l = [1, 3, 2, 4, 1, 6, 5]
l = [10, 1, 2, 4, 1, 6, 11]


peek= [];
for i in range(len(l)):
    if l[i] <= l[i+1 if i+1 < len(l) else i] :
        continue
    else :   
        peek.append(l[i])

print(peek)