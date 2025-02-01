from Node import Node

class singlylist:

    def __init__(self,list):
        if not list :
            self.head = None
            self.tail = self.head
        else:
            self.head = Node(list[0])
            self.tail = self.head
            for val in list[1:]:
                self.tail.next = Node(val)
                self.tail = self.tail.next

    def __str__(self):
        l = []
        def trav(lst):
            if lst.next is None:
                l.append(lst.data)
            else:
                l.append(lst.data)
                trav(lst.next)
        trav(self.head) if self.head else ''

        return ' -> '.join(map(str,l))
    

LL1 = singlylist([])
print(LL1)

# traversing on linked list using loops

