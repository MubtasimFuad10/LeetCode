def solution():
    nums=[1,3,4,2,8,9]
    nums.sort()
    for i in range(len(nums)):
        if nums[i]==nums[i+1]:
            return True
        return False
print(solution())
def hashset(): #optimal solution
    nums=[2,3,4,2]
    hashset= set()
    for i in nums:
        if i in hashset:
            return True
        hashset.add(i)
    return False

print(hashset())











