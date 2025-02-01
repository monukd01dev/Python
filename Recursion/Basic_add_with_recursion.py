def f(x,y):
    if x == 0 : 
        return y 
    else:
       return f(x-1,y+1)

print(f(2,5))