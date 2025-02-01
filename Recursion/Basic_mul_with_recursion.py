'''
i/p : 2,3
i/o : 6
you have to perform the multiplication with recursion
'''


def f(m,n):
    if n==1: return m

    elif n==0 : return 0

    else :
        return m + f(m,n-1)
    
print(f(2,5))