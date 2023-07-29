'''
The Problem 4.2: Minimal Tree
________________________________
Given a sorted (increasing order) array with unique interger elements,
write an algorithm to create a binary search tree with minimal height.
'''

'''
We have an array/list with properties
[1, 2, 3, 4, 5, 6, 7, .....]
-sorted in ascending order 
-Unique integer elemetns

We want to use this array to create a binary search tree with min height


A binary search tree is:
A binary tree is a tree in which each node has 2 children
                1
            2       3
        4      5 6      7 

A binary search tree is a binary tee in which every node fits a specific 
ordering propery e,g, all left descendents are less than or equal to 
all right descendants. 

'''
'''
Pseudocode
_______________________________
If A is empty, then return Null
find the mid element, and make it root
Divide the array into two sub-arrays, left part of the mid element, and right part of the mid element
recursively perform the same task for the left subarray and right subarray.
'''

class BST:
    '''
    Constructor

    '''
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

    def insert(self):
        return None
    
    def pop(self):
        