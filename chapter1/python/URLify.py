'''
Write a methd to replace all spaces in a string strings with %20. 
You may assume that the string has sufficient space to hold additional characters, 
and that you are given the true length of the string

Example
Input: "Mr John Smith ", 13
Output: "Mr%20John%20Smith"
'''

'''
Method: 
Read string into array and then do a for loop to say 
If char equals a space replace char with %20
'''
def  replaceSpace(s1):
    check = []
    n = len(s1)
    for i in range(n):
        check.append(s1[i])
    
    for j in range(n):
        if check[j] == ' ':
            check[j] = "%20"
    print(check)
replaceSpace(s1 = "hard math  ")

'''
A better solution to do in-place assuming that we have extra space in the input string. 
We first count the number of spaces in the input string. 
Using this count,we can find the length of the modified (or result) string. 
 After computing the new length we fill the string in-place from the end. 
'''

def replaceSpace2(s2):
    max_char = 1000

    string = s2.strip() #remove leading and trailing spaces

    #find original length
    n = len(string)

    #count spaces 
    space_count = string.count(' ')

    #find new length 
    new_length = n + space_count*2

    #new length must be smaller than length of string provided
    if new_length > max_char:
        return -1
    
    #start filling character from end 
    index = new_length - 1

    string = list(string)

    #Fill string array
    for f in range(n - 1, new_length - 1):
        string.append('0')

    #fill rest of string from end
    for j in range(n-1, -1, -1):
        #inserts %20 in place of space
        if string[j] == ' ':
            string[index] = '0'
            string[index - 1] = '2'
            string[index - 2] = '%'
            index = index - 3
        else:
            string[index] = string[j]
            index -= 1

    fixed = ''.join(string)
    print(fixed)

replaceSpace2(s2 = " hello world ha ")



