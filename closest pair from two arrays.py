class Solution:
    def printClosest(self, arr, brr, n, m, x):
        i = 0
        j = m - 1  # Start from the end of brr
        res = []
        closest = float('inf')

        while i < n and j >= 0:
            s = arr[i] + brr[j]

            if abs(s - x) < abs(closest - x):
                closest = s
                res = [arr[i], brr[j]]

            if s > x:
                j -= 1
            else:
                i += 1

        return res
