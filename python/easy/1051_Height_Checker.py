from typing import *
class Solution:
    # 14.2 MB, less than 71.05% of Python3 online submissions for Height Checker.
    # 14.2 MB, less than 71.05% of Python3 online submissions for Height Checker.
    def heightChecker(self, heights: List[int]) -> int:
        return sum(now != hope for now, hope  in zip(heights, sorted(heights)))


if __name__ == "__main__":
    so = Solution()
    print(so.heightChecker(heights = [5,1,2,3,4]))