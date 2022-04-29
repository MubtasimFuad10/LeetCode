def hashset(): #optimal solution
    nums=[2,3,4,1]
    hashset= set()
    for i in nums:
        if i in hashset:
            return True
        hashset.add(i)
    return False

print(hashset())











