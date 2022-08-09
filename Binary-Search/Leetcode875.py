from typing import List
import math


def minEatingSpeed(piles, h):
    l, r = 1, max(piles)
    res = r
    while l <= r:
        k = (l + r) // 2
        hours = 0
        for p in piles:
            hours += math.ceil(p / k)

        if hours <= h:
            res = min(res, k)
            r = k - 1  # right pointer to be in mid-1
        else:
            l = k + 1  # left pointer to be in mid+1

    return res
if __name__=="__main__":
    list1=list(map(int, input().split()))
    h=int(input())
    print(minEatingSpeed(list1, h))
