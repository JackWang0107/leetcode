from sys import prefix
from typing import *
class Solution:
    # 76 ms, faster than 57.13% of Python3 online submissions for Peak Index in a Mountain Array.
    # 15.3 MB, less than 82.83% of Python3 online submissions for Peak Index in a Mountain Array.
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        if_peak_found = False
        n = len(arr)//2
        left = 0
        right = len(arr)
        while not if_peak_found:
            if arr[n - 1] < arr[n] < arr[n+1]:
                left = n
                n = (n + right ) // 2
                if_peak_found = False
            elif arr[n - 1] > arr[n] > arr[n+1]:
                right = n
                n = (n + left) // 2
                if_peak_found = False
            elif arr[n -1] < arr[n] > arr[n+1]:
                if_peak_found = True
        return n


if __name__ == "__main__":
    so = Solution()
    print(so.peakIndexInMountainArray([40,48,61,75,100,99,98,39,30,10]))

