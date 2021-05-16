from typing import *
class Solution:
    #  68 ms, faster than 66.96% of Python3 online submissions for How Many Numbers Are Smaller Than the Current Number.
    # 14.4 MB, less than 45.73% of Python3 online submissions for How Many Numbers Are Smaller Than the Current Number
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        nums_sorted = sorted(nums)
        return [ nums_sorted.index(i) for i in nums]

if __name__ == "__main__":
    so = Solution()
    print(so.smallerNumbersThanCurrent([8,1,2,2,3]))