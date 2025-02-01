#WAP to find the GCD and LCD 

'''Basically GCD and LDC have a ralation  LCM(a,b)×GCD(a,b)=a×b '''

def GCD(a,b):
    min_val = min(a,b)
    while min_val >= 1:
        if a%min_val == 0 and b%min_val == 0:
            return min_val
        min_val -= 1


def LCD(a,b) : 
    return abs(a*b)//GCD(a,b)

print(GCD(4,6))

print(LCD(4,6))

