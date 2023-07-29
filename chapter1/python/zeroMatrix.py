'''
Write an algorithm such that if an element in an M x M matrix is 0.
 Its entirerow and column are set to 0

 17, 74, 102
'''

#17 - if you just cleared the rows and columns as you found 0s, 
# youd wind up clearing the whole matrix. try finding the cells with 0s first 
# before making any changes to matrix

#74 - can u use O(n) space instead of O(n^2).
#  What information do you really need from lis of cells that are 0

#102 - you need data storage to mantain a list of rows and columns that need to be 0ed.
#  can u chanfe space to O(1) by using matrix itself for data storage

'''
Example
_______
Input: 1 2 3
       4 5 6
       7 8 0

Output:
       1 2 0
       4 5 0
       0 0 0
'''

def setZeroes(matrix):
    #Space complexity O(1)
    rows, cols = len(matrix), len(matrix[0])
    rowZero = False

    #determine which rows/columns need to be zero
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 0:
                matrix[0][c] = 0 # Mark the first row of the column as 0
                if r > 0:
                  matrix[r][0] = 0 #Mark the first coloumn of the row as 0
                else:
                    rowZero = True #Mark that the first row contains as 0
    #Set the elements to 0 based on the marks in the first row and column
    for r in range(1, rows):
        for c in range(1, cols):
            if matrix[0][c] == 0 or matrix[r][0] == 0:
                matrix[r][c] = 0
    
    #Set the first column to 0 if the first element is 0
    if matrix[0][0] == 0:
        for r in range(rows):
            matrix[r][0] = 0
        
    #Set the first row to 0 if any element in it is 0
    if rowZero:
        for c in range(cols):
            matrix[0][c] = 0

    return matrix

x = setZeroes(matrix= [[1, 2, 3], [4, 5, 6], [7, 8, 0]])

print(x)