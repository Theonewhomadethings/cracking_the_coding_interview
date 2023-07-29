'''
________________________________
The Problem : Delete Middle Node
________________________________
Implement an algorithm to delete a node in the middle 
(i.e., any node but the first and last node, not necessarily the exact middle) 
of a singly linked list, given only access to that node. 
_______
EXAMPLE
_______ 
Input: the node c from the linked list a - >b- >c - >d - >e- >f 

Output: nothing is returned, but the new linked list looks like a->b->d->e-> f 
Hints: #72
'''

'''
__________
Pseudocode
__________
1. Initialise two pointers: Slow and Fast to the head of the Linked List.
2. Traverse the Linked List using the Fast pointer, moving 2 steps at a time and the slow pointer moving one step at a time.
 Stop when the fast pointer reaches the end of the list. This step helps determine the middle node of the Linked List.
3. Once the traversal is comeplete, the slow pointer is the middle node.
4. To delete the middle node, update the next pointer of the node before the middle node to point to the node after the middle node.
If the linked list only has 2 nodes, make the head point to the second node
5. Delete the middle node (free the memory occupied by it)
6. Return or print the modified Linked List.

'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
def delete_middle_node(head):
    '''
    Time Complexity : O(n) where n is th number of nodes in the linked list. In worst case we need to visit each node once as we are traversing the linked list to find the middle node. The traversal is performed using 2 pointers.
    Space Complexity: O(1) uses constant amount of additional space regardless of input linked list as we are using temporary variables to keep track of nodes during the traversal. No additional data structures are used.

    1. Initialise two pointers: Slow and Fast to the head of the Linked List.
2. Traverse the Linked List using the Fast pointer, moving 2 steps at a time and the slow pointer moving one step at a time.
 Stop when the fast pointer reaches the end of the list. This step helps determine the middle node of the Linked List.
3. Once the traversal is comeplete, the slow pointer is the middle node.
4. To delete the middle node, update the next pointer of the node before the middle node to point to the node after the middle node.
If the linked list only has 2 nodes, make the head point to the second node
5. Delete the middle node (free the memory occupied by it)
6. Return or print the modified Linked List.
    '''
    Fast = head
    Slow = head
    prev = None

    #Traverse the linked list to find the middle node
    while Fast is not None and Fast.next is not None:
        #Move the fast pointer 2 steps forward
        Fast = Fast.next.next 
        #Keep track of the nod ebefore the slow pointer 
        prev = Slow 
        #Move the slow pointer one step forward
        Slow = Slow.next
    
    #Update the pointer before the middle node to point to the node after the middle.
    prev.next = Slow.next #update the pointer before the middle node to point the node after
    del Slow #Delete the middle node and free the memory occupied by it
    #return the modified Linked list
    return head

def print_linked_list(head):
    current = head
    while current is not None:
        print(current.data, end = " -> ")
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

print("Original linked list")
print_linked_list(head)


print("Linked list with middle node deleted")

head = delete_middle_node(head)

print_linked_list(head)


