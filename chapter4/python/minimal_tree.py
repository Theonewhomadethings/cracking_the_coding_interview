'''
The Problem 4.2: Minimal Tree
________________________________
Given a sorted (increasing order) array with unique interger elements,
write an algorithm to create a binary search tree with minimal height.
'''


class TreeNode:
    #First define a class for the binary tree nodes
    def __init__(self, value = 0, left = None, right = None):
        self.value = value #value of the node
        self.left = left # left child
        self.right = right #right child


#Define the function to create the minimal height BST. Takes a sorted array as input and returns the root node of the tree.
def minimal_tree(sorted_array):
    #base case: Return None if the array is empty
    if not sorted_array:
         return None
        
    #Calculate the mid index
    mid = len(sorted_array) // 2
    #create the root node with the mid val
    root = TreeNode(value = sorted_array[mid])

    #recursively build the left subtree
    root.left = minimal_tree(sorted_array[:mid])
    #recursively build the right subtree
    root.right = minimal_tree(sorted_array[mid+1:])

    #return the root node of the constructed tree
    return root

#function to print the tree in a pre-order traversal to test the solution
def pre_order_traversal(node):
    if node:
        print(node.value, end =  " ")
        pre_order_traversal(node.left)
        pre_order_traversal(node.right)


#Test the code by creating a min height tree from a sorted array and printing its elemetns
sorted_array = [1, 2, 3, 4, 5, 6, 7]
root = minimal_tree(sorted_array)
print("Pre-order traversal of the minimal height tree:")
pre_order_traversal(root)