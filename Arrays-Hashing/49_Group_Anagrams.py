from collections import defaultdict
from itertools import count


def groupAna():
    s=input()
    strs=s.split()
    res=defaultdict(list) #mapping charCount to list of Anagrams
    
    for string in strs:
        count=[0]*26 #a..z
        for c in string:
            count[ord(c)-ord("a")]+=1
        res[tuple(count)].append(string)
    return res.values()

print(groupAna())
        
