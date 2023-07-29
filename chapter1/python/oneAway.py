'''
The problem:
Therre are 3 types of edits that can be performed on strings.
Replace a character, remove a character, insert a character
Given 2 strings, write a function to check if they are 1 edit or 0 edits away
'''
'''
Example:
pale, ple -> true
pales, pale -> true
pale, bale -> true
pale, bake -> false
'''

'''
Efficient solution 1:
Simulatneusly traverse both strings and keep track of count of different characters.
Steps:
length of string 1 =m, length of string2 = n
1) if difference between m and n is more than 1 return False

2) Initialise count at zero

3) Start traversing both strings from first character.
    a) if current characters dont match then 
        i) Increment count of edits
        ii) If count became more than one, return False
        iii) If length of string is 1 more, then only possible edit
            is to remove characters.Therefore move ahead in larger string
        iv) If length is same than only possible edit is to change a character. Move ahead in both strings
    b) else, move ahead in bith strings.
'''

def oneEditVer1(s1, s2):
    m = len(s1) #length of string 1 IS m
    n = len(s2) #length of string 2 is n

    if abs(m-n) > 1:
        return False

    count = 0 #initialize count
    i = 0
    j = 0

    while ( i < m) and ( j < n):
        #if current characters dont match
        if s1[i] != s2[j]:
            if count > 0:
                return False
            #if length of 1 string is more than 
            #only possible edit is to remove a character
            if m > n:
                i += 1
            elif m < n:
                j += 1
            else:
                 i += 1
                 j += 1
            #increment count of edits
            count += 1
        #if characters match
        else:
            i += 1
            j += 1

    #if last character is extra in any string   
    if i < m or j < n:
        count += 1
    
    return count <= 1


y = oneEditVer1(s1 = "yes", s2 = "yes")
print(y)