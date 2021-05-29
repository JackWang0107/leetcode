from typing import *
class Solution:
    # 48 ms, faster than 80.79% of Python3 online submissions for Maximum Product of Two Elements in an Array.
    # 14.3 MB, less than 70.58% of Python3 online submissions for Maximum Product of Two Elements in an Array.
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        return (nums[-2]-1) * (nums[-1]-1)


if __name__ == "__main__":
    so = Solution()
    print(so.maxProduct([1,5,4,5]))