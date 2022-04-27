from typing import Counter
def isAnagram():
    s=input()
    t=input()
    if len(s) != len(t):
        return False
    
    countS, countT ={}, {} #hashmap/dictionaries/hashtables

    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)   # if the character doesnt exists in the hashmap. so skip keyerror we need to use get() function.
        countT[t[i]] = 1 + countT.get(t[i], 0)
    
    for c in countS:
        if countS[c] != countT.get(c,0):
            return False
    return True

print(isAnagram())

def isAnagram2(): #oneliner code
    s=input()
    t=input()
    return Counter(s)==Counter(t)

print(isAnagram2())
        





