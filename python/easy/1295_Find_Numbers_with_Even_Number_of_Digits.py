from typing import *
class Solution:
    # 36 ms, faster than 99.98% of Python3 online submissions for Find Numbers with Even Number of Digits.
    # 14 MB, less than 97.63% of Python3 online submissions for Find Numbers with Even Number of Digits.
    def findNumbers(self, nums: List[int]) -> int:
        ans = 0
        for n in nums:
            if len(str(n)) % 2 == 0:
                ans += 1
        return ans

    # 40 ms, faster than 99.48% of Python3 online submissions for Find Numbers with Even Number of Digits.
    # 14.2 MB, less than 89.16% of Python3 online submissions for Find Numbers with Even Number of Digits.
    def findNumbers(self, nums: List[int]) -> int:
        return sum( 1 for n in nums if len(str(n)) % 2 == 0)


if __name__ == "__main__":
    so = Solution()
    print(so.findNumbers(nums = [12,345,2,6,7896]))