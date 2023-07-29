'''
How would you design a stack which in addition push and pop.
Has a function min which returns the minimum element
push, pop and min should operate in O(1) time.
'''
'''
27 - Observe that the minimum element doesnt change very often. It only changes when a smaller element is added or when the smallest element is popped.
59 - What if we kept track of extra data at each stack node?
78 - Consider having each node know the minimum of its substack. All element beneath it including itself.
pg 111 is 3.3 problempg 621 is hints
'''

class minStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val:int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
    
stack1 = minStack()

stack1.push(-5)
stack1.push(1)
stack1.push(2)
stack1.push(3)


print(stack1.getMin())