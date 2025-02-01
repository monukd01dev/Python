from Node import Node
import inspect
from takeinput import takinginput

# print(inspect.getsource(Node))



def createLinkedList(l):
    '''
        Time complexity of this function is O(n^2)
        cause everytime it adds an element we have to traverse the whole list to find the tail/last_element
    '''
    head = None
    for item in l:
        new_node = Node(item)
        if head is None:
            head = new_node
        else:
            curr_node = head
            while curr_node.next is not None:
                curr_node = curr_node.next
            curr_node.next= new_node
    return head

def creLinkedList(l):
    '''
        Time complexity of this function is O(n)
        cause each node is traversed only once
    '''
    if not l:
        return None
    head = Node(l[0])
    tail = head
    for val in l[1:]:
        tail.next = Node(val)
        tail = tail.next

    return head

def printLL(ll):

    if ll.next is None:
        print(ll.data,end=" ")
    else:
        print(ll.data,end=' ')
        printLL(ll.next)
        
if __name__ == '__main__':
    # printLL(createLinkedList((takinginput())))
    # printLL(creLinkedList((takinginput())))

    myList = creLinkedList([20,30,40,50,60])
    print(myList)