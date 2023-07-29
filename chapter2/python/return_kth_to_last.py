'''
_________
The Problem : Return Kth to Last 
_________
Implement an algorithm to find the Kth to last element of a singly linked list.
'''
'''
Hints: 
8 - What if you knew the linked list size. What is the diffrence between finding the Kth to last element and finding the Xth element.
25  - If you do know the linked list size can you compute it. How does this affect the run time.
41  - Try implementing it recursively. If you could find the (K-l)th to last element, can you 
find the Kth element? 
67 - You might find it useful to return multiple values. Some languages don't directly support 
this, but there are workarounds in essentially any language. What are some of those 
workarounds?
126 - Can you do it iteratively? Imagine if you had two pointers pointing to adjacent nodes 
and they were moving at the same speed through the linked list. When one hits the end 
of the linked list, where will the other be?
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def kth_to_last(head, K):
    '''
    _________
    Algorithm: Kth to last element of a singly linked list
    _________
    1. Intialize two pointers: Fast and Slow pointing to the head of the singly linked list
    2. Prompt the user to enter the value of K
    3. Move to the Fast pointer K steps ahead in the linked list
    4. If the Fast pointer becomes null. e.g. It reaches the end of the linked list, it means K is greater than the length of the list.
    In this case it means we return an error of an appropriate response
    5. Move both the Fast and Slow pointer simulataenously, one step at a time,
    until the Fast pointer reaches the end of the linked list.
    6. The slow pointer will now be at the Kth to last element of the linked list.
    7. Return the value of the element pointed to by the slow pointer.
    '''
    Fast = head
    Slow = head #both pointers intialized at head

    for i in range(K): #Initialise the fast pointer to be K steps ahead in linked list with this loop
        if Fast is None:
            #fast pointer has become null so it means K is greater than the length of the list
            print("Error. The K value you have inputted exceeds the length of the list. Please try a smaller K int value. ")
            return
        Fast = Fast.next 
    
    while Fast is not None:
        Fast = Fast.next
        Slow = Slow.next #Move both fast and slow pointers simulateneously untill fast pointer reaches the end of the linked list
    return Slow.data #at this point slow pointer is now at Kth to last position. Return the value of the element.

def print_linked_list(head):
    current = head
    while current is not None:
        print(current.data, end = " ")
        current = current.next
    print()

head = Node(1)
node1 = Node(2)
node2 = Node(3)
node3 = Node(4)
node4 = Node(5)

head.next = node1
node1.next = node2
node2.next = node3
node3.next = node4

print("Linked list original")
print_linked_list(head)

K = int(input("Please input of the Kth element you want: "))
ans = kth_to_last(head, K)
print("The Kth to last element in a singly linked list is:", ans)