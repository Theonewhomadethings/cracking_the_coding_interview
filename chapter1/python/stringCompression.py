'''
Implement a method to perform basic string compression using the counts of repeated characters.
For example the string aabcccccaaa would become a2b1c5a3.
If the compressed string would not become smaller than the original string than 
method returns original string.
Assume string has only uppercase and lowercase letters.
'''

'''
Pseudocode for string traversal method
Traverse string aaabcccccaaa iteratively.
In a loop count the a characters with a counter. 
When the character index moves to a different character it saves the count of the
a to a dictionary in the 1st value positon and the 1st key position is an a character.
Then repeat with the other characters to obtain the dictionary
{"a": 3 , "b": 1, "c": 5, "a": 2}
for the string aaabcccccaa
then print out the dictionary in a new string format to print
stringNeq = "a3b1c5a2"
'''

from collections import Counter

def stringCompressionVer1(s1):
    counts = Counter(s1)
    
    #need to figure out how to get
stringCompressionVer1(s1 = "aaabcccccaaa")


'''
Method 2:
The string Builder or a list to build the compressed string instead of 
concatenating the strings directly. This avoids the overhead of string concatenation.

'''

def compressedString(s1):
    #initalise an empty list to store compressed characters and counts
    compressed = []
    #initalize count
    count = 0 
    #set the current char to first char of the
    current_char = s1[0]

    for char in s1:
        #if current charcter is same as previous one
        if char == current_char:
            #increment count
            count += 1
        else:
            #if the current character is different from prev one 
            #add the compressed version of the previous count to the list
            compressed.append(current_char + str(count))
            #update the current character to the new character
            current_char = char
            #reset count for new char
            count = 1
    
    #add the last character and its count to the list
    compressed.append(current_char + str(count))
    #Join the compressed characters and the counts into a single string
    compressed_string = "".join(compressed)
    
    #if the compressed string is longer than original string or equal
    if len(compressed_string) >= len(s1):
        #return original string
        return s1
    else:
        return compressed_string

x = compressedString(s1 = "aaabcccccaaa")
print(x)