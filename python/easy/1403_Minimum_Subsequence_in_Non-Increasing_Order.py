from typing import *
class Solution:
    # 80 ms, faster than 27.44% of Python3 online submissions for Minimum Subsequence in Non-Increasing Order.
    # 14.2 MB, less than 62.78% of Python3 online submissions for Minimum Subsequence in Non-Increasing Order.
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        for i in range(len(nums)):
            if sum(nums[:i]) > sum(nums[i:]):
                return nums[:i]
        return nums    # ensure single value list will be returned


if __name__ == "__main__":
    so = Solution()
    print(so.minSubsequence(nums = [6]))