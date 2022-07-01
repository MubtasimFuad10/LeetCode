def solve(n):
    dp1, dp2 = 1,1
    for i in range(n-1):
        temp=dp1
        dp1=dp1+dp2
        dp2=temp
    return dp1

if __name__=="__main__":
    n=int(input())
    print(solve(n))