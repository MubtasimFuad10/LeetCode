def twosum():
    nums=[2,7,11,15]
    target=9
    prevMap ={} #val : index
    for index, value in enumerate(nums): #enumurate tracks both the index and the values
        diff = target - value
        if diff in prevMap:
            return [prevMap[diff], index]
        prevMap[value]=index

print(twosum())