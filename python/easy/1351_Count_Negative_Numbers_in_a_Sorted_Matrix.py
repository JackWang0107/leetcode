from typing import *
class Solution:
    # 160 ms, faster than 5.47% of Python3 online submissions for Count Negative Numbers in a Sorted Matrix.
    # 15 MB, less than 91.75% of Python3 online submissions for Count Negative Numbers in a Sorted Matrix.
    def countNegatives(self, grid: List[List[int]]) -> int:
        return sum( 1 for row in grid for num in row if num < 0)


    # 132 ms, faster than 10.61% of Python3 online submissions for Count Negative Numbers in a Sorted Matrix.
    # 15 MB, less than 91.75% of Python3 online submissions for Count Negative Numbers in a Sorted Matrix.
    def countNegatives(self, grid: List[List[int]]) -> int:
        totoal_number = 0
        row_length = len(grid[0])
        for row in grid:
            for idx, num in enumerate(row):
                if num < 0:
                    totoal_number += row_length - idx
                    break
        return totoal_number

if __name__ == "__main__":
    so = Solution()
    print(so.countNegatives(grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]))