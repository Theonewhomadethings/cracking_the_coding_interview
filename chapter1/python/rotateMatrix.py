'''
__________
The Problem
__________
Given an image represented by an N x N matrix, where each pixel in the image is 4 bytes. 
Write a method to rotate the image by 90 degrees. Can you do this in place?
'''
'''
Hints
51 - Try think about it layer by layer. can you rotate a specific layer

100 - rotating a specific layer would just mean swapping the values in four arrays. 
If you were asked  to swap the values in 2 arrayss could you do this. can you extend it to 4 arrays
'''

'''
Example
Input:
1 2 3 
4 5 6
7 8 9  
Output:
7 4 1 
8 5 2
9 6 3
'''

'''
Method 1 
Time: O(n^2)
Space: O(1)

An N x N matrix will have floor(N/2) square cycles.
For example a 3 by 3 matrix will have 1 cycle.
The cycle is formed by its 1st row, last column, last row and 1st column.
For each square cycle we swap elements involved with the corresponding cell in the matrix in the clockwise direction.
We just need a temperorary variable for this
'''

def rotateMatrixVer1(matrixA):
    n = len(matrixA[0])
    for i in   range(n // 2):
        for j in range(i, n - i - 1 ):
            temp = matrixA[i][j]
            matrixA[i][j] = matrixA[n - 1 - j][i]
            matrixA[n - 1 - j][i] = matrixA[n - 1 - i][n - 1 - j]
            matrixA[n - 1 - i][n - 1 - j] = matrixA[j][n - 1 - i]
            matrixA[j][n - 1 - i] = temp
    return matrixA


x = rotateMatrixVer1(matrixA = [[1, 2, 3, 4],
                            [5, 6, 7, 8],
                            [9, 10, 11, 12],
                            [13, 14, 15, 16]])


y = rotateMatrixVer1(matrixA = [[1, 2, 3],
                            [5, 6, 7],
                            [9, 10, 11]])

print(y)


'''
Second method:Performing the 90 degree rotation in Layers
Starting from the outer layer and moving towards the inner layers of the matrix.
For each layer, you perform a series of elements swaps to achieve the rotation
time complexity: O(n^2 / 2) which simplifies to O(n^2)

Outline of the algorithm
1) Iterate over the layers of the matrix. Each layer corresponds to a square formed by the outer elements of the matrix.
2) For each layer, perform a series of four-way swaps to rotate the elements. You can achieve this by swapping
elements in a cyclic manner. e.g. swap the top left element with the bottom right element.
3) Continue this swapping precess with all the elements in the current layer until you reach the centre of the matrix.

By performing the rotation in layers you elimate redundant swaps and acheive the same result with a more efficient algorithm.

'''

def rotateMatrixVer2(matrixB):
    n = len(matrixB)
    #Iterate over the layers of the matrix
    for layer in range(n // 2):
        first = layer 
        last = n - 1 - layer 

        #iterate over the elements in the current layer
        for i in range(first, last):
            offset = i - first
            #store the value in the top of the element
            top = matrixB[first][i]
            #left -> top
            matrixB[first][i] = matrixB[last - offset][first]
            #bottom -> left
            matrixB[last - offset][first] = matrixB[last][last - offset]
            #right -> bottom
            matrixB[last][last - offset] = matrixB[i][last]
            #top -> right
            matrixB[i][last] = top
        return matrixB
    
z = rotateMatrixVer2(matrixB = [[1, 2, 3], 
                                [4, 5, 6], 
                                [7, 8, 9]])

print(z)