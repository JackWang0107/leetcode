from typing import *
class Solution:
    # 68 ms, faster than 52.37% of Python3 online submissions for Sum of All Odd Length Subarrays.
    # 14.1 MB, less than 76.80% of Python3 online submissions for Sum of All Odd Length Subarrays.
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        i = 1
        sums = 0
        while i <= len(arr):
            temp = [arr[idx:idx+i] for idx in range(len(arr) - i + 1)  ]
            sums += sum([sum(sub_arr) for sub_arr in temp])
            i = i  + 2
        return sums

    #  32 ms, faster than 97.72% of Python3 online submissions for Sum of All Odd Length Subarrays.
    # 14.2 MB, less than 49.35% of Python3 online submissions for Sum of All Odd Length Subarrays.
    # This is not my solution, if you want to know more about the formular, please check the link under here:  
    # https://leetcode.com/problems/sum-of-all-odd-length-subarrays/discuss/1053840/python-3-fastest-solution-with-O(n)-time-complexity
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        Sum=0
        for i in range(len(arr)):
            Sum += (
                (
                    (
                        (i + 1) * (len(arr) - i) +1
                        ) // 2
                    ) * arr[i]
                )
        return Sum

if __name__ == "__main__":
    so = Solution()
    print(so.sumOddLengthSubarrays(arr = [10,11,12]))