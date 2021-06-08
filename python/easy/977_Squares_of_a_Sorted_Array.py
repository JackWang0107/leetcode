from typing import *
class Solution:
    # 268 ms, faster than 20.65% of Python3 online submissions for Squares of a Sorted Array.
    # 16.3 MB, less than 31.16% of Python3 online submissions for Squares of a Sorted Array.
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return [i**2 for i in sorted(nums, key=lambda x:x**2)]


if __name__ == "__main__":
    so = Solution()
    print(so.sortedSquares(nums = [-7,-3,2,3,11]))