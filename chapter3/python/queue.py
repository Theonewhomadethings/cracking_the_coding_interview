class Node:
    def __init__(self, data, next_node = None):
        '''
        Initializes a new node object.

        Args:
            data: The data to be stores in the node
            next_node: Reference to the next node in the linked list (default is None)
        '''
        self.data = data 
        self.next_node = next_node

    def __str__(self):
        '''
        Returns a string representation of the node

        returns:
            The string representation of the nodes data
        '''
        return str(self.data)
    

class LinkedList:
    def __init__(self, head = None):
        '''
        Initializes a new linked list object

        Args:
            head: The first node in the linked list
        '''
        self.head = head

    def insert(self, node):
        '''
        Inserts a node at the end of the linked list

        Args: 
            node: The node to be inserted
        '''
        if self.head is None:
            self.head = node
            return
        current_node = self.head 
        while current_node.next_node is not None:
            current_node = current_node.next_node
        current_node.next_node = node

    def pop_head(self):
        '''
        Removes and returns the head node of the linked list.

        Returns:
            The head node that has been removed or None if the list is empty
        '''
        if self.head is not None:
            head_to_pop = self.head 
            self.head = self.head.next_node
            return head_to_pop
        
        return None

    def size(self):
        '''
        Returns the size (number of nodes) of the linked list

        Returns:
            The size of the linked list.
        '''
        current_node = self.head 
        size = 0
        while current_node is not None:
            size += 1
            current_node = current_node.next_node
        return size

