'''
The Problem: Intersection
_________________________
Given 2 singly linked lists, determine if the 2 lists intersect.
Return the intersecting node. Note that the intersection is defined based on reference, not value.
That is, if the kth node of the first linked list is the exact same node as the jth node
of the second linke
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def intersection(headA, headB):
    '''
    '''
    l1, l2 = headA, headB
    while l1 is not l2:
        l1 = l1.next if l1 else headB
        l2 = l2.next if l2 else headA
    return l1.data

def print_linked_list(head):
    current = head
    while current is not None:
        print(current.data, end = " ")
        current = current.next
    print()

headA = Node(4) #linked list A = [4,1,8,4,5]
node1A = Node(1)
node2A = Node(8)
node3A = Node(4)
node4A = Node(5)
headA.next = node1A
node1A.next = node2A
node2A.next = node3A
node3A.next = node4A

headB = Node(5) #linked list B = [5,6,1,8,4,5]
node1B = Node(6)
node2B = Node(1)
node3B = Node(8)
node4B = Node(4)
node5B = Node(5)
headB.next = node1B
node1B.next = node2B
node2B.next = node3B
node3B.next = node4B
node4B.next = node5B

node4A.next = node2B

print(" Linked List A")
print_linked_list(headA)

print(" Linked List B")
print_linked_list(headB)

print(intersection(headA, headB))
