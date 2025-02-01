from LinkedList import creLinkedList

myList = creLinkedList([20,30,40,50,60])

#traversing of linked list with loop no recursion

def printList(lst):
    #handling the edge case
    if not lst:
        print(None)
        
    else:
        current_node = lst
        while current_node.next:
            print(current_node.data,"->",end=' ')
            current_node = current_node.next
        print(None)
        
printList(myList)