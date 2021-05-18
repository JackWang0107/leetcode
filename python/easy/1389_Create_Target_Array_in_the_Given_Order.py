from typing import *
class Solution:
    # 32 ms, faster than 73.30% of Python3 online submissions for Create Target Array in the Given Order.
    # 14.4 MB, less than 11.57% of Python3 online submissions for Create Target Array in the Given Order.
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        ans = []
        [ans.insert(idx, value) for idx, value in zip(index, nums)]
        return ans

    # 32 ms, faster than 73.30% of Python3 online submissions for Create Target Array in the Given Order.
    # 14.2 MB, less than 45.26% of Python3 online submissions for Create Target Array in the Given Order.
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        ans = []
        for idx, value in zip(index, nums):
            ans.insert(idx, value)
        return ans

if __name__ == "__main__":
    so = Solution()
    print(so.createTargetArray(nums = [1,2,3,4,0], index = [0,1,2,3,0]))