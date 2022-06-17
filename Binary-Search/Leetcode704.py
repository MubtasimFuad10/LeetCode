def solve(nums, target):
    l, h =0, len(nums)-1
    while(l<=h):
        mid=l+((h-l)//2) # (l + r) // 2 can lead to overflow in java or cpp language . python can handle "(l+h)/2" but better to use this "l+((h-l)//2)"
        if target > nums[mid]:
            l=mid+1
        elif target < nums[mid]:
            h=mid-1
        else:
            return mid
    return -1

if __name__=="__main__":
    n=int(input())
    nums=list(map(int, input().split()))
    target=int(input())
    print(solve(nums, target))