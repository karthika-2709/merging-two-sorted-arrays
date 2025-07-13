class Solution:
    def sortInWave(self, arr):
        n=len(arr)
        i=0
        j=1
        while j<n:
            if(arr[i]<arr[j]):
                arr[i],arr[j]=arr[j],arr[i]
                i=i+1
                j=i+2
            return
