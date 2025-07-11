class Solution:
    def sumClosest(self, arr, target):
        arr.sort()
        n = len(arr)
        low = 0
        high = n - 1
        closest = float('inf')
        res = []

        while low < high:
            s = arr[low] + arr[high]

            # If this pair is closer to target
            if abs(s - target) < abs(closest - target):
                closest = s
                res = [arr[low], arr[high]]
            elif abs(s - target) == abs(closest - target):
                # Prefer pair with maximum absolute difference
                if abs(arr[low] - arr[high]) > abs(res[0] - res[1]):
                    res = [arr[low], arr[high]]

            # Move pointers
            if s < target:
                low += 1
            else:
                high -= 1

        return res if res else []
