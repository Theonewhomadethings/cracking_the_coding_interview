'''
Task:  Given 2 strings, write a method to decide if one is a permutation of the other
Hints: #1, #84, #122, #131
'''
'''
Permutation definition = dj_dthe set of all the strings, 
 that contains the same characters as the original string, 
 but the order of the arrangement of the characters can be different
'''
'''
Method 1: Sorting Approach
1) Sort both strings
2) Compare the sorted strings
Time: O(nlogn)
Space: O(1)
'''
def checkPermutation(s1, s2):
    n = len(s1)
    m = len(s2)

    ##If the lengths of the 2 strings dont equal each other then they cant be permutations of each other
    if (n != m):
        return False 

    #sort both strings and define new variables for these sorted strings
    sortS1 = sorted(s1)
    str1 = "".join(sortS1)
    sortS2 = sorted(s2)
    str2 = "".join(sortS2)

    #comparison of the sorted strings
    for i in range(n):
        if (str1 != str2): #Since they are sorted they are the exact same word now. So if the char arent equal 
            return False   #The program returns False as they cant be permutations of each other
    
    return True # Hence they are permutations of each other as we have compraed the 2 sorted strings
                # and they are the same length

checkPermutation(s1 = "Happy", s2 = "Sad")


'''
Second method: Counting the characters and Comparing
This method assumes the set of possible characters is small.
It is assumed that the characters can be stored using 8 bits and there are 256 possible chars
1) Create count arrays of size 256 for both strings. Intialize all values at 0
2 Iterate through every character of both strings and increment the count of character in the corresponding
count arrays 
3) Compare count arrays.If both count arrays are the same then return True
Time: O(n) 
Space: O(n)
'''

def checkPermutation2(s1, s2):
    numberOfChars = 256 
    
    #creating 2 count arrays and intializing all element values as zero
    count1 = [0] * numberOfChars
    count2 = [0] * numberOfChars


    #For each character in input string, increment count in the corresponding count array 
    for i in s1:
        count1[ord(i)] += 1

    for j in s2:
        count2[ord(j)] += 1

    #If both strings are of different length, then they cant be permutations of each other can they
    if (len(s1)) != (len(s2)):
        return 0
    
    #Comparison of the count arrays
    for x in range(numberOfChars):
        if count1[x] != count2[x]:
            return 0
        
    return 1


checkPermutation2(s1 = "Happy", s2 = "Sad")