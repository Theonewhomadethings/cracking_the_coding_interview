'''
Is Unique: Implement an algorithm to determine if a string has all 
unique characters. What if you cannot use additional data structures? 
'''
#Hints: #44, #117, #132
#44 -> Try a Hash Table
#117 -> Could a bit vector be useful?
#132 -> Can you solve it in 0(N lo g N) time? What might a solution like that look like?


# Brute force #Time = O(n^2), #Memory = O(1)
#Brute force uses 2 loops with variables i and j and Comaprison techniques.
def uniqueStringBrute(string):
    for i in range(len(string)): 
        for j in range(i+1, len(string)):
            if string[i] == string[j]:
                print("Not unique")
                return False

    print("all chars in string are unique")
    return True


#niqueStringBrute(string = "wwww")

def uniqueStringSort(string1):
    '''
    Sorting approach
    Sorting based on ASCII values of characters
    '''
    #string = yellow
   # string = ellowy
    string2 = sorted(string1)
    for i in range(len(string2) - 1):
        if (string2[i] == string2[i+1]):
            print("Not unique")
            return False
    print("all chars in string are unique")    
    return True

uniqueStringSort(string1="yellow") 