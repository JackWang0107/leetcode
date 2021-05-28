from typing import *
class Solution:
    # 108 ms, faster than 56.16% of Python3 online submissions for Matrix Diagonal Sum.
    # 14.2 MB, less than 98.80% of Python3 online submissions for Matrix Diagonal Sum.
    def diagonalSum(self, mat: List[List[int]]) -> int:
        ans = 0
        length = len(mat)
        position = 0
        for i in range(length//2):
            ans += mat[i][position] + mat[i][length - position - 1] + mat[length - i - 1][position] + mat[length - i - 1][length - position - 1]
            position += 1
        if length % 2 != 0:
            ans += mat[ length //2][ length //2]
        return ans

if __name__ == "__main__":
    so = Solution()
    print(so.diagonalSum(mat = [[5]]))