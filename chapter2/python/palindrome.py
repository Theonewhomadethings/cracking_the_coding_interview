'''
_________________________
The problem : Palindrome:
_________________________
 Implement a function to check if a linked list is a palindrome. 
'''
'''
Hints:
5 - A palindrome is something which is the same when written forwards and backwards. What if you reversed the linked list

13 - Try using a stack

29 -  Assume you have the length of the linked list. Can you implement it recursively

61 -  In the recursive approach (we have the length of the list), the middle is the base case: isPermutation(middle) is true. 
The node x to the immediate left of the middle: What can that node to check if x -> raiddle - > y forms a palindrome ? 
Now suppose that checks out. What about the previous node 3? If x -> middle -> y is a palindrome, 
how can it check that a -> x -> middle - > y - > b is a palindrome

101 - Go back to that previous hint. Remember the ways to return multiple values . You can do this with a new class
'''
'''
Algorithm apporach:
1. Traverse the linked list and store each nodes value in an array or another linked list in the same order. This creates a copy of the original linked list.

2. Reverse the copy of the original linked list. You can do this by either creating a new linked list and inserting the nodes in reverse order or by manipulating the pointers of the existing linked list to reverse its direction.

3. Compare the reverse linked list with the original linked list by iterating through both lists simulataneously. Check if the values of the corresponding nodes are equal.

4. If all the values match, then the linked list is a palindrome. Return True. Otherwise, return False.

'''

class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None

def is_palindrome(head):
    #Step 1: Create a copy of the original linked list
    original_list = []
    current = head
    while current is not None:
        original_list.append(current.data)
        current = current.next

    #step 2: Reverse the copy of the original linked list
    prev = None
    current = head
    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current 
        current = next_node

    head = prev
    #Step 3: Compare the reversed linked list with the original linked list
    current = head
    for value in original_list:
        if current.data != value:
            return False
        current = current.next

    #Step 4: All values matched, the linked list is a palindrome
    return True

def print_linked_list(head):
    current = head
    while current is not None:
        print(current.data, end = " ")
        current = current.next
    print()

head = Node("A ")
node1 = Node("B")
node2 = Node("B")
node3 = Node("A")

head.next = node1
node1.next = node2
node2.next = node3

print("Original linked list:")
print_linked_list(head)

if is_palindrome(head) == True:
    print("The linked list is a palindrome")

else:
    print("The linked list is not a palindrome")