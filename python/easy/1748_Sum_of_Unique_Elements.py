from typing import *
class Solution:
    # 36 ms, faster than 50.68% of Python3 online submissions for Sum of Unique Elements.
    # 14.3 MB, less than 40.68% of Python3 online submissions for Sum of Unique Elements.
    def sumOfUnique(self, nums: List[int]) -> int:
        from collections import Counter
        ans = dict(Counter(nums))
        sums = 0
        for key, value in ans.items():
            if value == 1:
                sums += key
        return sums

    # 32 ms, faster than 79.11% of Python3 online submissions for Sum of Unique Elements.
    # 14 MB, less than 89.14% of Python3 online submissions for Sum of Unique Elements.
    def sumOfUnique(self, nums: List[int]) -> int:
        repeated_num = []
        added_num = []
        sums = 0
        for num in nums:
            if num in repeated_num:
                continue
            if num in added_num:
                repeated_num.append(num)
                sums -= num
                continue
            sums += num
            added_num.append(num)
        return sums


if __name__ == "__main__":
    so = Solution()
    print(so.sumOfUnique(nums = [1,2,3,2]))