

from git import TagReference
import numpy as np


def solve(matrix, target):
    rows, colmns = len(matrix) , len(matrix[0]) #[0] index beacuse no matter which index you want will give the same result of length of the column
    #print(rows, colmns)

    top , bott= 0, rows-1

    while(top <= bott):
        mid1 = top+(bott-top)//2 #the mid row of the matrix
        if target > matrix[mid1][-1]: #here we are checking the highest value(rightmost value) of the array
            top = mid1+1  #going down to the matrix gives us the larger values
        elif target < matrix[mid1][0]: # here we are checking the lowest value(leftmost value) of the array
            bott = mid1-1 #going top(previous row) will give us the smallest values
        else:
            break #it means the target value is in the current row

    #NOTE: This portion of binary search will give us the result which rows has the target values (TC= log(m))   

    if not (top <= bott): #returning false if the target value is not found in the array
        return False
    low, high = 0, colmns-1
    while(low<=high):
        mid2=low+(high-low)//2 #mid value of the specific row
        if target > matrix[mid1][mid2]:
            low=mid2+1
        elif target < matrix[mid1][mid2]:
            high=mid2-1
        else:
            return True
    return False
    #This portion of binary search will give us the target values position (TC=log(n))

    #NOTE:SO, TOTAL TIME COMPLEXITY OF THIS ALGORITHM IS O(log(m)+log(n)) where, m is the row and n is the colomn
    


if __name__ =="__main__":
    #taking user input is optional(I took for practice purposes)

    row=int(input())
    column=int(input())
    matrix=[[int(input()) for x in range(column)] for y in range(row)]
    #matrix values = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    print(matrix) #optional
    target=int(input())
    print(solve(matrix, target))
    
    
    
    
    
    
    
    #-->taking 2D array input using numpy


    # entries=list(map(int, input().split()))
    # matrix2=np.array(entries).reshape(row, column)
    # print(matrix2)
    # target=int(input())

    
 



















