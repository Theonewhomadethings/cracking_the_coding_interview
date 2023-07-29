class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def partition(head, partition):
    before_start = None
    before_end = None
    after_start = None
    after_end = None

    current = head
    while current is not None:
        next_node = current.next
        if current.data < partition:
            if before_start is None:
                before_start = current
                before_end = before_start
            else:
                before_end.next = current
                before_end = current
        else:
            if after_start is None:
                after_start = current
                after_end = after_start
            else:
                after_end.next = current
                after_end = current

        current.next = None
        current = next_node

    if before_start is None:
        return after_start

    before_end.next = after_start
    return before_start

def print_linked_list(head):
    current = head
    while current is not None:
        print(current.data, end=" ")
        current = current.next
    print()

# Creating the linked list: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1
head = Node(3)
head.next = Node(5)
head.next.next = Node(8)
head.next.next.next = Node(5)
head.next.next.next.next = Node(10)
head.next.next.next.next.next = Node(2)
head.next.next.next.next.next.next = Node(1)

print("Original Linked List:")
print_linked_list(head)

head = partition(head, partition=5)

print("Linked List after Partition Function:")
print_linked_list(head)
