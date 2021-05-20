from typing import *
from itertools import combinations
from functools import reduce
from operator import xor


class Solution:
    # 68 ms, faster than 70.76% of Python3 online submissions for Sum of All Subset XOR Totals.
    # 14.4 MB, less than 25.45% of Python3 online submissions for Sum of All Subset XOR Totals.
    def subsetXORSum(self, nums: List[int]) -> int:
        sums = sum(nums)
        for i in range(2, len(nums)+1):
            sums += sum([reduce(xor, i) for i in combinations(nums,i)])
        return sums


if __name__ =="__main__":
    so = Solution()
    print(so.subsetXORSum([3,4,5,6,7,8]))