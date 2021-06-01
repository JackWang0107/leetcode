from typing import *
class Solution:
    # 80 ms, faster than 58.31% of Python3 online submissions for Sort Array By Parity.
    # 15.2 MB, less than 22.91% of Python3 online submissions for Sort Array By Parity.
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even = []
        odd = []
        for num in nums:
            if num % 2 == 0:
                even.append(num)
            if num % 2 == 1:
                odd.append(num)
        even.extend(odd)
        return even
    
    # 68 ms, faster than 98.29% of Python3 online submissions for Sort Array By Parity.
    # 14.8 MB, less than 99.01% of Python3 online submissions for Sort Array By Parity.
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i = 0
        for j in range(len(nums)):
            if nums[j] %2 == 0:#irrespective of the number at ith position, we are swapping if number at j is even
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        return nums

if __name__ == "__main__":
    so = Solution()
    print(so.sortArrayByParity([0]))