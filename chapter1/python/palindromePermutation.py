'''
The problem:
Given a string, write a function to check if it is a permutation of a palindrome.
A palindrome is a word or phrase that is the same forwards and backwards;
A permutation is a rearangement of letters.
The palindrome does not need to be limited by just dictionary words.
'''

'''
The example:
Input: Tact Coa
Output: True
Reason: (permutations: "taco cat", "atco cta", etc...)
'''

'''
 it only needs to determine if it is possible to rearrange the letters into a palindrome.
'''
from collections import Counter

def palindromePermutation1(s1):
    #For a string to be a palindrome then every letter is mirrored around the centre of a string.
    #This means a collection of letters form a palindrome if there is at most one letter that has an odd count.

    #First step) Convert string to lower case and remove nonalphanumeric characters.
    #Use list comprehension to iterate over each character in the string and keep only those
    #whose string  .isalpha() returns true
    alpha_char = [x for x in s1.lower() if x.isalpha()]

    #count each letter
    counts = Counter(alpha_char)
    
    #count the number of letters with an odd count. If the count is 0 or 1 then a palindrome must be possible. 
    number_of_odd = sum(1 for letter, cnt in counts.items() if cnt%2)

    return number_of_odd <= 1

y = palindromePermutation1(s1 = "popl")
print(y)