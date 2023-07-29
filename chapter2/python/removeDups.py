'''
____________
The problem : Remove Dups
____________
Write code to remove duplicates from an unsorted linked list
'''

#head -> 1 > 5 -> 8 -> 2 -> 5 ->

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    '''
    Time complexity of this function is O(n). n is the number of nodes
    Space complexity O(k). k is the number of unique values.
    '''
def removeDuplicates(head): 
    if head is None:
        return head

    current = head
    #Set to stroe the seen values
    seen_values = {current.data}

    #Traverse the linked list
    while current.next is not None:
        if current.next.data in seen_values:
            #Duplicate node found, skip it by updating the next pointer
            current.next = current.next.next

        else:
            #Unique value encountered, add it to the set of seen values
            seen_values.add(current.next.data)
            #move to the next node
            current = current.next

    return head

#Helper function to print the linked list
def print_linked_list(head):
    current = head
    while current is not None:
        print(current.data, end = " ")
        current = current.next
    print()

head = Node(3)
node1 = Node(1)
node2 = Node(4)
node3 = Node(2)
node4 = Node(2)
node5 = Node(4)

head.next = node1
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print("Original Linked List: ")
print_linked_list(head)

head = removeDuplicates(head)

print("Linked List after removing duplicates: ")
print_linked_list(head)



