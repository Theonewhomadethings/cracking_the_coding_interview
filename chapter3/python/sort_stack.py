'''
The problem: Sort Stack
_______________________
Write a program to sort a stack such that the smallest items are on the top.
You cam use an additional temporary stack, but you may not copy the elements into
any other data structure such as an array. 
The stack supports the operations: Push Pop, Peek, isEmpty

Hints:

15 - One way of sorting an array is to iterate through the array and insert each 
element into a new array into a sorted order. Can you do this with a stack

32 - Imagine you sorted stack is sorted. Can you insert elements into it in sorted order.
You might need some extra storage. What could you use for extra storage.

43 - Keep the secondary stack in sorted order, with the biggest elements on top. Use the primary stack for additional storage. 
'''
import unittest
from stack import Stack


class SortedStack:
    def __init__(self):
        #Initilize the main and temp stack
        self.stack = Stack()
        self.temp_stack = Stack()

    def push(self, item):
        #If the main stack is empty or the item is smaller than the top element
        # #push directly onto the main stack 
        if self.is_empty() or item < self.peek():
            self.stack.push(item)
        else:
            #While the main stack is not empty and the item is greater than the top element,
            #move the top elements from the main stack to the temporary stack.
            while self.peek() is not None and item > self.peek():
                self.temp_stack.push(self.pop())
            
            #Push the item onto the main stack
            self.stack.push(item)
            #Move the elements from the temporary stack back to the main stack
            while not self.temp_stack.is_empty():
                self.stack.push(self.temp_stack.pop())

    def pop(self):
        #Pop and return the top element from the main stack
        return self.stack.pop()
    
    def peek(self):
        #Return the top element from the main stack without removing it
        return self.stack.peek()
    
    def is_empty(self):
        #Check the main stack is empty
        return self.stack.is_empty()

#example 
#create an instance of the sorted stack class
sorted_stack = SortedStack()

#Push some items onto the stack
sorted_stack.push(5)
sorted_stack.push(2)
sorted_stack.push(9)
sorted_stack.push(1)
sorted_stack.push(7)

#Check if the stack is empty
print(sorted_stack.is_empty())

print(sorted_stack.peek())
print(sorted_stack.pop())
print(sorted_stack.peek())