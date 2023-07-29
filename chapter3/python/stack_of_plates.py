'''
The Problem: Stack Of Plates 
____________________________
Imagine a stack of plates. If the stack gets too high, it might topple.
In real life, we would likely start a new stack when the previous stack
exceeds some threshold. Implement a data structure SetOfStacks that mimics this.
SetOfStacks should be composed of several stacks and should create a new stack 
once the previous once exceeds capacity. SetOfStacks.push() and SetOfStacks.pop()
should behave identically to a single stack (pop() should return the same values as
if there were just a single stack)
Extension:
Implement a function popAt(index) which performs a pop operation on a specific sub-stack
'''

'''
Hints:

64 - You will need to keep track of the size of each substack. When one stack is full
, you may need to create a new stack.

81 - Popping an element at a specific substack will mean that some stacks that aren't
at full capacity. Is this an issue> Theres no right answer. 
'''
#Space complexity in the worst case O(N*M) where N represents the total number  of elements stores in the setofstacks.
class SetOfStacks:
    def __init__(self, capacity):
        #Main stack that holds individual stacks
        self.stack = [] 
        #list to stroe individual stacks
        self.stacks = []  
        #error handling if capacity is less than one which doesnt make sense for stack data structure
        if capacity < 1:
            raise NameError("A stack capacity must be greater than one.")
        else:
            self.capacity = capacity

    #time O(1)
    def push(self, val):
        #check to see if the main stack is empty
        if self.stack == []:
            #create a new stack and add it to the list of stacks
            self.stacks.append([val])
        else:
            #check if the last stack is at capacity
            if len(self.stack[-1]) >= self.capacity:
                #create a new stack and add it to the main stack
                self.stack.append([val])
            else:
                #add the value to the last stack
                self.stack[-1].append(val)

    #time O(1)
    def pop(self):
        #check if the main stack is empty 
        if self.stack == []:
            raise NameError("Can't pop an empty stack")
        else:
            #get the last item from the last stack
            popped_data = self.stack[-1][-1]
            #check if the last stack has only one item
            if len(self.stack[-1]) == 1:
                #remove the last stack
                del self.stack[-1]
            else:
                #remove the last item from the last stack
                del self.stack[-1][-1]
                #return the popped item
            return popped_data

    #Pop operation on a specific sub stack
    '''
    Note!!  Popping an element at a specific substack will mean that some stacks that aren't
at full capacity. Is this an issue??? Theres no right answer. 
    '''
    def popAt1(self, index):
        #If empty individual stack
        if self.stacks == []:
            raise NameError("Can't pop an empty stack")
        
        elif index - 1 > len(self.stacks):
            raise NameError("Index is out of range")
        
        else:
            #pops the last element in selected index of main stack
            popped_data = self.stacks[index - 1][-1]
            if len(self.stacks[index - 1]) == 1:
                #If stack length equals one just delete the last element
                del self.stacks[-1]
            
            elif len(self.stacks) == index:
                del self.stacks[-1][-1]

            else:
                self.stacks[index - 1][-1] = self.stacks[index][0]

                for i in range(index, len(self.stacks)):
                    #Move each element forward/up
                    for j in range(0, len(self.stacks[i]) - 1):
                        self.stacks[i][j] = self.stacks[i][j+1]
                    if i < len(self.stacks)-1 :
                        self.stacks[i][-1] = self.stacks[i+1][0]

                del self.stacks[-1][-1]

                #If length of stack is empty, delete it.
                if len(self.stacks[-1]) == 0:
                    del self.stacks[-1]
                
        return popped_data

    def popAt2(self, index):
        #Check if the index is valid
        if index < 1 or index > len(self.stacks):
            raise NameError("Index is out of range")
        
        #Calculate the actual index of the substack in the stacks list
        stack_index = index - 1

        #Check if the seleceted sub-stack is empty
        if len(self.stacks[stack_index]) == 0:
            raise NameError("You can't pop from an empty substack")
        
        #Pop the element from the selected sub stack
        popped_data = self.stacks[stack_index].pop()

        #Adjust the stacks after popping the element
        for i in range(stack_index, len(self.stacks) - 1):
            #Move the first element of each subsequent sub stack to the previous substack
            self.stacks[i].append(self.stacks[i+1].pop(0))

        #Remove the last sub-stack if it becomes empty
        if len(self.stacks[-1]) == 0:
            del self.stacks[-1]

        
        return popped_data