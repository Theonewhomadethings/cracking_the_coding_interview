'''
___________
The problem:
___________
assume you have a method isSubstring which checks if one word is a substring of another.
Given 2 strings. s1 and s2, write code to check if if s2 is a rotation of s1 using only one call to isSubstring. 

Example
"waterbottle" is a rotation of "erbottlewat"

34, 88, 104
'''


def string_rotation(s1, s2):
    #time O(n)
    #Space O(n)
    #Concatentated string has length 2nd where n is the length of s1
    if len(s1) == len(s2) != 0: #checks the lengths of both strings are equal and non zero
        return s2 in s1 * 2 #uses in operator to check if s2 is a substring of s1 repeated twisce s1 * 2
    return False
x = string_rotation(s1= "waterbottle", s2 = "erbottlewat")
print(x)