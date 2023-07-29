class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
    
    def is_empty(self):
        return self.head is None
    
    def append(self, data):
        new_node = Node(data)

        if self.is_empty():
            #If the list is empty, set the new node as the head
            self.head = new_node
        else:
            #Traverse to the end of the list and add the new node
            current = self.head
        
            while current.next:
                current = current.next
            current.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        if self.is_empty():
            #If the list is empty set the new node as the head
            self.head = new_node
        else:
            #set the new node as the head and link it to the previous head
            new_node.next = self.head
            self.head = new_node
        
    def insert_after(self, prev_node, data):
        if not prev_node:
            #If the previous node is not present, return
            print("Previous node is not present in the list.")
            return
        new_node = Node(data)
        #Insert the new node between prev_node and its next node 
        new_node.next = prev_node.next
        prev_node.next = new_node
        
    def delete(self, data):
        if self.is_empty():
            #If the list is empty return
            print("The list is empty")
            return
        if self.head.data == data:
            #If the head node is to be deleted, set the next node as the new head
            self.head = self.head.next
        
        current = self.head
        while current.next:
            if current.next.data == data:
                #Skip the node to be deleted by adjusting the next pointer
                current.next = current.next.next
                return
            current = current.next
        print(f"{data} is not found in the list.")

    def display(self):
        if self.is_empty():
            print("The list is empty")
            return

        current = self.head 
        while current:
            #Print the data of each node in the list
            print(current.data, end= " -> ")
            current = current.next
        print("None")


linked_list = LinkedList()

linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.display()
linked_list.prepend(0)
linked_list.display()