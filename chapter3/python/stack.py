class Stack:
    def __init__(self):
        #Initialize an empty list to store the stack elements
        self.items = []

    def is_empty(self):
        #Check of the stack is empty
        return len(self.items) == 0
    
    def push(self, item):
        #Add an item to the top of the stack
        self.items.append(item)

    def pop(self):
        #Remove and return the item at the top of the stack
        return self.items.pop()
    
    def peek(self):
        if self.items:
            #Return the item at the top of the stack without removing it 
            return self.items[-1]
        return None
    
    def __len__(self):
        #Return the length of the stack (number of elements)
        return len(self.items)
    
    def __bool__(self):
        #return true if the stack is not empty, false otherwise
        return bool(self.items)
    
