# a node have atleast two parts 
'''
1. Data
2. Next => Reference to the next node

'''

class Node : 
    def __init__(self,data):
        self.data = data
        self.next = None 
    # def __str__(self):
    #     return f'{self.data}'
    def __str__(self):
        return f'{self.data} -> {self.next}'


    