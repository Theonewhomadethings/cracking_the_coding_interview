
'''
THE PROBLEM: Three In One
_________________________
Describe how you can use a single array to implement 3 stacks

Hints
_____
2 - A stack is simply a data structure in which most recently added lements are removed first. 
Can you simulate a single stack using an array. Remember that there are many possible solutions
and tradeoffs of each.

12 - 

38 - 

58 - 
'''

arr1 = []
    #Simulate a single stack using an array
    #Stack - LIFO (Last In First Out). Use stack of plates metaphor.
    # 4 operations: PUSH(), POP(), PEEK(), IsEmpty()

def push():
    '''
    Inserts the element at the top of the stack Time: O(1)
    '''
    arr1.append("hello")
    arr1.append(8)
    arr1.append("c")

def pop():
    '''
    Deletes the topmost element of the stack. Time: O(1)
    '''
    arr1.pop()

def peek():
    '''
    Returns a reference to the topmost element of the stacl. Time: O(1)
    '''
    if len(arr1) == 0:
        return None
    else:
        return arr1[-1]
    

def IsEmpty():
    '''
    Returns whether the stack is empty. Time O(1)
    '''
    if len(arr1) == 0:
        return "is empty"
    else:
        return "Not empty"
push()

print("Stack after push()", arr1)
pop()
pop()
print("Stack after 2 POP()", arr1)

print("The topmost element is", peek())

print("Implementation of isEmpty() tells us that stack: ", IsEmpty())
