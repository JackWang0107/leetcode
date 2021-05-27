from typing import *
class Solution:
    # Manipulation on list such as changing value costs more time than reading
    # 124 ms, faster than 82.18% of Python3 online submissions for Minimum Operations to Make the Array Increasing.
    # 14.9 MB, less than 81.12% of Python3 online submissions for Minimum Operations to Make the Array Increasing.
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)-1):
            if nums[i] >= nums[i+1]:
                ans += nums[i] - nums[i+1] + 1
                nums[i+1] = nums[i] + 1
        return ans

    # 104 ms, faster than 99.92% of Python3 online submissions for Minimum Operations to Make the Array Increasing.
    # 14.9 MB, less than 81.12% of Python3 online submissions for Minimum Operations to Make the Array Increasing.
    def minOperations(self, nums: List[int]) -> int:
        ans, pointer=0,0
        for i in nums:
            # if the next number is greater than pointer, then, just make pointer point to next number
            if pointer < i:
                pointer = i
            # if the number is less or equal to pointer, next number will become `pointer + 1`, thus, `pointer + 1 -i`  steps are needed
            else:
                pointer += 1
                ans+=pointer - i
        return ans
if __name__ == "__main__":
    so = Solution()
    print(so.minOperations(nums = [1, 1, 1]))