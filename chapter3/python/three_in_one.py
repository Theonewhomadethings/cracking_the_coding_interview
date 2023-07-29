
'''
THE PROBLEM: Three In One
_________________________
Describe how you can use a single array to implement 3 stacks

Hints
_____
2 - A stack is simply a data structure in which most recently added lements are removed first. 
Can you simulate a single stack using an array. Remember that there are many possible solutions
and tradeoffs of each.

12 - We could simulate 3 stacks in an array by just allocating the first third of the array to the
 first stack, the second third to the second stack and the final third to the third stack. 
One might be much bigger than the others, though. Can we be more flexible with the divisions?

38 - If you want to allow for flexible divisions, you can shift stacks arround. Can you ensure that all available capacity is used.


58 - Try thinking about the array as circular such that end of thearray wraps around to the start of the array
'''


class MultiStack:
    def __init__(self, stacksize):
        self.numstacks = 3
        #create an array of size stack size * numstacks
        self.array = [0] * (stacksize * self.numstacks)#
        #Create a list to store the sizes of each stack
        self.sizes = [0] * self.numstacks

        self.stacksize = stacksize

    def Push(self, item, stacknum):
        #Check if the stack is already full. If it is raise an error message
        if self.IsFull(stacknum):
            raise Exception("Stack is Full")
        #Increment the size of the stack
        self.sizes[stacknum] += 1
        #Add the item to the top of the stack
        self.array[self.IndexOfTop(stacknum)] = item 

    def Pop(self, stacknum):
        #Check if the stack is empty
        if self.IsEmpty(stacknum):
            raise Exception("Stack is empty")
        #Get the value at the top of the stack 
        value = self.array[self.IndexOfTop(stacknum)]
        #Set the top of the stack to 0 (empty)
        self.array[self.IndexOfTop(stacknum)] = 0
        #decrement the size of the stack
        self.sizes[stacknum] -= 1
        return value

    def Peek(self, stacknum):
        #Check if the stack is empty
        if self.IsEmpty(stacknum):
            raise Exception("Stack is empty")
        #return the value at the top of stack
        return self.array[self.IndexOfTop(stacknum)]

    def IsEmpty(self, stacknum):
        #Check if the size of the stack is 0 (empty)
        return self.sizes[stacknum] == 0
    
    def IsFull(self, stacknum):
        #Chec if the size of the stack is equal to the stack size
        return self.sizes[stacknum] == self.stacksize
    
    def IndexOfTop(self, stacknum):
        #Calculate the offset of the top of the stack
        offset = stacknum * self.stacksize 
        #Return the index of the top of the stacl
        return offset + self.sizes[stacknum] - 1
    
def ThreeInOne():
    #Create an Instance of Multistack with stack size 2
    newstack = MultiStack(3)
    #Check if stack 1 is empty (should be True)
    print(newstack.IsEmpty(1))
    #Push item 3 to stack 1
    newstack.Push(3, 1)
    #Peek the top item of stack (should be 3)
    print(newstack.Peek(1))
    #Check if the stack 1 is empty (should be false)
    print(newstack.IsEmpty(1))
    #push item 2 to stack 1
    newstack.Push(2, 1)
    #Peek the top item of stack 1 ( Should be 2 )
    print(newstack.Peek(1))
    #Pop the top item from stack 1 (should be 2)
    print(newstack.Pop(1))
    #peek the top item if stack 1 after pooping (should be 3)
    print(newstack.Peek(1))
    #Push item 3 to stack 1 again
    newstack.Push(3, 1)

ThreeInOne()