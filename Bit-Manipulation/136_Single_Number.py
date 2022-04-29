def hashset1(): #optimal solution
    nums=[4,1,2,4,1]
    hashset= set()
    for i in nums:
        if i in hashset:
            hashset.remove(i)
            print(i)


hashset1()