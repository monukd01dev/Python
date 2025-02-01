'''
i/p : 4 
o/p : 1234

also write the programm for reverse printing order

'''

def wholeNum(n):
    if n == 1 :
        print(n,end="")
    else:
        wholeNum(n-1)
        print(n,end="")

wholeNum(4)

def wholeNumRev(n):
    if n == 1 :
        print(n,end="")
    else:
        print(n,end="")
        wholeNumRev(n-1)

wholeNumRev(4)