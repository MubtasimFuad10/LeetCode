def solve_BS(nums, target):
    low, high = 0, len(nums)-1
    while(low<=high):
        mid=(low+high)//2
        if target==nums[mid]:
            return mid
        
        if nums[low] <= nums[mid]:
            if target > nums[mid] or target < nums[low]:
                low=mid+1
            else:
                high=mid-1
        else:
            if target < nums[mid] or target > nums[high]:
                high=mid-1
            else:
                low=mid+1
    return -1

if __name__=="__main__":
    nums=list(map(int, input().split()))
    target=int(input())
    print(solve_BS(nums, target))