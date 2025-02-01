'''
i/p : 5632
i/o : 16
'''

def f(n):
    if n<10:
        return n 
    else :
        return n%10 + f(n//10)
    
print(f(5632))