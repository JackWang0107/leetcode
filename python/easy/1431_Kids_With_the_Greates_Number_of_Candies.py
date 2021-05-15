from typing import *
class Solution:
    # 36 ms, faster than 77.15% of Python3 online submissions for Kids With the Greatest Number of Candies
    # 14.2 MB, less than 79.83% of Python3 online submissions for Kids With the Greatest Number of Candies.
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maximum = max(candies)
        return [ True if candy + extraCandies >= maximum else False for candy in candies]


if __name__ == "__main__":
    so = Solution()
    print(so.kidsWithCandies(candies = [4,2,1,1,2], extraCandies = 1))