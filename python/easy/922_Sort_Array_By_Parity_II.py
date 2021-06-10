from typing import *
class Solution:
    # 252 ms, faster than 20.15% of Python3 online submissions for Sort Array By Parity II.
    # 16.7 MB, less than 47.34% of Python3 online submissions for Sort Array By Parity II.
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        ans =[None] * len(nums)
        odd_pointer = 1
        even_pointer = 0
        for i in nums:
            if i & 1 == 1:
                ans[odd_pointer] = i
                odd_pointer += 2
                continue
            ans[even_pointer] = i
            even_pointer += 2
        return ans

    # 276 ms, faster than 16.78% of Python3 online submissions for Sort Array By Parity II.
    # 16.2 MB, less than 93.80% of Python3 online submissions for Sort Array By Parity II.
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        odd_pointer = 1
        even_pointer = 0
        n = len(nums)
        while odd_pointer < n and even_pointer < n:
            while odd_pointer < n and nums[odd_pointer] & 1 == 1:
                odd_pointer += 2
            while even_pointer < n and nums[even_pointer] & 1 == 0:
                even_pointer += 2
            if odd_pointer < n and even_pointer < n:
                nums[odd_pointer], nums[even_pointer] = nums[even_pointer], nums[odd_pointer]
        return nums

if __name__ == "__main__":
    so = Solution()
    print(so.sortArrayByParityII([2,3]))