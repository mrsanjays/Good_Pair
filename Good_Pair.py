""""
Given an array A and an integer B. A pair(i, j) in the array is a good pair if i != j and (A[i] + A[j] == B). Check if any good pair exist or not.
"""
class Solution:
    @staticmethod
    def good_pair(arr,k):
        n=len(arr)
        for i in range(n):
            for j in range(i+1,n):
                if arr[i]+arr[j]==k:
                    return 1
        return 0
if __name__ == '__main__':
    array=list(map(int,input().split()))
    k=int(input())
    ob=Solution()
    print(ob.good_pair(array,k))