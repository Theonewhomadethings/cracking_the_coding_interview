#Linked list implementation of a Queue data structure.


'''
A linked list node
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''
A class to represent a queue
The queue. 
The front stores the front node of Linked list and rear stores the last node of the Linked List.
'''
class Queue1:
    def __init__(self):
        self.front = self.rear = None

    def isEmpty(self):
        return self.front == None
    
    #Method to add an item to the queue
    def enQueue(self, item):
        temp = Node(item)
    
        if self.rear == None:
            self.front = self.rear = temp
            return 
        self.rear.next = temp
        self.rear = temp

    def deQueue(self):
        if self.isEmpty():
            return
        temp = self.front 
        self.front = temp.next

        if (self.front == None):
            self.rear = None
        

class Queue2:
    def __init__(self):
        #Initialize the fronT/head pointer of the queue to none
        self.head = None
        #Intitlize the rear / last pointer of the queue to none
        self.last = None

    def enQueue(self, data):
        #If the queue is empty 
        if self.last is None:
            #Create a new node and make it to the front/head of the queue
            self.head = Node(data)
            #Make it to the rear / last of the queue
            self.last = self.head
        #else when the queue is not empty
        else: 
            #Create a new node and append it to the end of the queue 
            self.last.next = Node(data)
            #Updaet the rear / last pointer to the newly added node
            self.last = self.last.next


    def deQueue(self):
        #If the queue is empty
        if self.head is None:
            #return none as there is nothing to dequeue
            return None
        #If the queue is not empty 
        else:
            #get the data of the front / head node
            to_return = self.head.data
            #move the front /head pointer to the next node
            self.head = self.head.next
            #If after dequeing, the queue becomes empty
            if self.head is None:
                #Update the rear/last pointer to None as well
                self.last = None
            #return the dequeued data
            return to_return
        
    def isEmpty(self):
        #If the front / head pointer is none, indicating its empty
        if self.head == None:
            return None

    def peek(self):
        #If the queue is empty return none
        if self.head is None:
            return None
        else:
            #if the queue is not empty return the front/head node
            return self.head.data, self.head.timestamp