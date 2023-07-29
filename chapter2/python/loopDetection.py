'''
____________________________
The problem : Loop Detection
____________________________
Given a circular linked list, implement an algorithm that returns the node at the beggining of the loop.

Definition of a ciruclar loop - A (corrupt) linked list in which a nodes next pointer to an earlier node,
 so as to make a loop in the linked list.

Example:
Input:  A -> 8 -> C -> D -> E -> C (the same C as earlier)
Output: C
'''

class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None

#part 1 implementation of function
#This code returns true if there is a cycle in Linked list

def if_cycle(head):
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next 
        if slow == fast:
            return True
    return False  

def cycle_linked_list(head):
    slow = head
    fast = head
    loop_detected = False

    #Detect the cycle using Floyds cucle-finding algorithm 
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            loop_detected = True
            break
    
    #If no cycle detected, return None
    if not loop_detected:
        return "There is no cycle present"

    #Move slow pointer to head and advance both pointers until they meet 
    slow = head
    while slow != fast:
        slow = slow.next 
        fast = fast.next
    
    #return the node at the beggining of the loop
    return slow
    

def print_linked_list(head):
    current = head
    while current is not None:
        print(current.data, end = " ")
        current = current.next
    print()


head = Node("A")
node1 = Node(8)
node2 = Node("C")
node3 = Node("D")
node4 = Node("E")
node5 = Node("X")

head.next = node1
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print("Original linked list")
print_linked_list(head)

node5.next = node2 #Connect the last node back to the c node in a circular ways

res = cycle_linked_list(head)
if res == "There is no cycle present":
    print(res)
else:
    print(res.data)