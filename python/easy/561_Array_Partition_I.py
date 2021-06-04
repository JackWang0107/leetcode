from typing import *
class Solution:
    # 328 ms, faster than 7.55% of Python3 online submissions for Array Partition I.
    # 16.7 MB, less than 94.50% of Python3 online submissions for Array Partition I.
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return sum(min(i,j) for i,j in zip(nums[::2], nums[1::2]))

    # 260 ms, faster than 75.45% of Python3 online submissions for Array Partition I.
    # 16.7 MB, less than 94.50% of Python3 online submissions for Array Partition I.
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return sum(nums[::2])

if __name__ == "__main__":
    so = Solution()
    print(so.arrayPairSum(nums = [6,2,6,5,1,2]))