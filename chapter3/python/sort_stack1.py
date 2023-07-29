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
from stack import Stack

#colourful code implementation
#not sure if this implementation is correct as it uses list data stuctures and no stacks
def sortStack(stack):
    #temporary varaible
    curr = 0

    #temp stack
    temp = []

    #while stack is not empty
    while stack != []:
        #curr holds value popped from end of stack
        curr = stack.pop()

        #If temp is empty or curr is greater than the last element in 
        #temp, append curr to temp
        if len(temp) == 0 or curr > temp[len(temp)-1]:
            temp.append(curr)

        else:
            j = True

            while j:
                #if curr is less than last element in temp pop off last element and
                #append element back to stack
                if curr < temp[len(temp)-1]:
                    stack.append(temp.pop())
                    #if temp is empty, stop while loop
                    if len(temp) == 0:
                        j = False
                
                else:
                    j = False
            temp.append(curr)

        #append temp to stack to flip in ascending order
        stack.append(temp)

        return stack
    
#print(sortStack([5, 3, 2, 6, 21]))

#original way
def sortStackV2(stack):
    #Create a temporary stack
    tempStack = Stack()

    #While the original stack is not empty
    while not stack.is_empty():
        #get the top element of the original stack
        temp = stack.peek()
        #Remove the top element from the original stack
        stack.pop()

        #While the temporary stack is not empty and its top element is less than the current element
        while not tempStack.is_empty() and int(tempStack.peek()) < int(temp):
            #Push the top element of the temporary stack  to the orginal stack
            stack.push(tempStack.peek())
            #remove the top element from the temporary stack
            tempStack.pop()

        #Push the current element to the temporary stack
        tempStack.push(temp)

    #return the sorted stack
    return tempStack

'''
#More object orientated and pythonic way utilizing the prinicples of 
encapsulation and composition
'''
'''
This class represents a stack that maintain its elements in a sorted order with the
smalles elements at the top
'''
class SortedStack1:
    def __init__(self):
        #Create an empty stack
        self.stack = Stack()
        #Create an empty temporary stack
        self.temp_stack = Stack()

    def push(self, item):
        #Whie the main stack is  not empty and the item is greater than the top element of the stack
        while not self.stack.is_empty() and item > self.stack.peek():
            #Move the top element of the main stack to the temp stack 
            self.temp_stack.push(self.stack.pop())
        #Push the item to the main stack
        self.stack.push(item)

        #While the temporary stack is not empty
        while not self.temp_stack.is_empty():
            #Move the elements back from the temporary stack to the main stac
            self.stack.push(self.temp_stack.pop())

    def pop(self):
        #Pop and return the top element of the stack
        return self.stack.pop()
    
    def peek(self):
        #return the top element of the stack but keep it in the stack
        return self.stack.peek()
    
    def is_empty(self):
        #check if the main stack is empty
        return self.stack.is_empty()