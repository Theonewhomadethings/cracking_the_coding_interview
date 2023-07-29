'''
The problem : Sum Lists
_______________________
 You have two numbers represented by a linked list, where each node
contains a single digit. The digits are stored in reverse order,
 such that the Vs digit is at the head of the list. Write a function 
 that adds the two numbers and returns the sum as a linked list. 
EXAMPLE 
Input: (7- > 1 -> 6) + (5 -> 9 -> 2).That is,617 + 295. 
Output: 2 -> 1 -> 9. That is, 912. 
FOLLOW UP 
Suppose the digits are stored in forward order. Repeat the above problem. 
EXAMPLE 
Input: (6 -> 1 -> 7) + (2 -> 9 -> 5).That is, 617 + 295, 
Output:9 -> 1 -> 2,Thatis,912. 
Hints: #7, #30, #71 #95, #109 
'''


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def sum_list(head1, head2):
    '''
    '''
    carry = 0
    result = None
    current = None 

    while head1 is not None or head2 is not None:
        _sum = carry

        if head is not None:
            _sum += head1.data
            head1 = head1.next
        
        if head2 is not None:
            _sum += head2.data
            head2 = head2.next
        
        if _sum >= 10:
            carry = 1
            _sum = _sum % 10
        else:
            carry = 0
        
        node = Node(_sum)

        if result is None:
            result = node 
            current = node

        else:
            current.next = node
            current = current.next 
    if carry > 0:
        current.next = Node(carry)
    
    return result


def print_linked_list(head):
    current = head
    while current is not None:
        print(current.data, end = " -> ")
        current = current.next 
    print()

def reverse_linked_list(head):
    prev = None
    current = head

    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

def sum_lists_forward(head1, head2):
    reverse_head1 = reverse_linked_list(head1)
    reverse_head2 = reverse_linked_list(head2)
    reverse_sum = sum_list(reverse_head1, reverse_head2)
    forward_sum = reverse_linked_list(reverse_sum)
    return forward_sum

head = Node(7)
node1 = Node(1)
node2 = Node(6)

head.next = node1
node1.next = node2

head1 = Node(5)
node11 = Node(9)
node21 = Node(2)

head1.next = node11
node11.next = node21

print_linked_list(head)

print_linked_list(head1)

sumgame = sum_list(head, head1)

print("The sum of the 2 linked lists is: ")
print_linked_list(sumgame)


print("The sum of the linked lists (forward order):")
sum_result = sum_lists_forward(head, head1)
print_linked_list(sum_result)