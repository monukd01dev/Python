'''
i/n : 2
o/p : IndiaInida
i/n : 3
o/p : IndiaInidaIndia

Note: Have to done this with recursion 
'''

def india(n):
    #baseCase 
    if n==1:
        print('India',end='')
        return
    else:
        print('India',end='')
        india(n-1)

india(4)