'''
The Problem: Queue Via Stacks
_____________________________
Implement a MyQueue class which implements a queue using two stacks
PG 111
Hints:

98 - The major difference between a queue and a stack is in the order of elements. 
A queue removes the oldest item and a stack removes the newest item.
How could you remove the oldest item from a stack if you had access to the newest item?


114 - We can remove the oldest item from a stack by repeatedly removing the newest item 
(inserting those into the temporary stack) until we get down to one element.
Then, after we have retrieved the newest item, putting all the elements back.
The issue with this is that we are doing several pops in a row that will require O(N) each time.
Can we optimize for scenarios where we might be do several pops in a row.
pG 671 FOR HINTS
'''

#Implementing a queue using 2 stacks
#n is the number of items in queue
#Time O(1) amortized run time 
#Space O(n)

import unittest

from stack import Stack

class QueueViaTwoStacks:
    def __init__(self):
        #Initialize two stacks
        self.new_stack = Stack()  #deals with enqueues and dequeues
        self.old_stack = Stack() #deals with recieving data inputted

    '''
    The shift stacks method is used to shift elements from the new stack to the old stack only when the old stack is empty.
    This ensures that the oldest item is always at the top of the old stack when you need to perform dequeueing or peeking operations.
    '''
    def shift_stacks(self): 
        #Shift elements from new stack to the old stack
        if self.old_stack.is_empty():
            while not self.new_stack.is_empty():
                self.old_stack.push(self.new_stack.pop())


    '''
    The enqueue method simply pushes the value to the new stack
    '''
    def enQueue(self, value):
        #add an element ot the queue by pushing it to the new stack
        return self.new_stack.push(value)
    
    '''
    The dequeue method checks if the queue is empty then calls shift stacks to ensure that the oldest item is at the top of the old stack,
    and finally removes and returns the top element from the old stack.
    '''
    def deQueue(self):
        #Remove and return the element at the front of the queue
        if self.is_empty():
            return False
        self.shift_stacks()
        return self.old_stack.pop()

    '''
    The peek method is similar to  dequeue but does not remove the element from the queue. It also checks if the queue is empty,
    shifts the stacks if necessary and returns the top element from the old stack.
    '''
    def peek(self):
        #return the element at the front of the queue without removing anything
        if self.is_empty():
            return False
        self.shift_stacks()
        return self.old_stack.peek()
    
    def is_empty(self):
        #check if the queue is empty
        return len(self) == 0
    
    def __len__(self):
        #return the size of the queue (number of elements)
        return len(self.new_stack) + len(self.old_stack)
    
    