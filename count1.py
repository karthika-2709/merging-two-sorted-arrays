class Solution:
    def countOnes(self, arr):
        n=len(arr)
        c=0
        for i in range(0,n):
            if arr[i]==1:
                c+=1
                i+=1
        return c
