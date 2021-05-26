from typing import *
class Solution:
    # Easy numpy solution
    # 112 ms, faster than 8.55% of Python3 online submissions for Cells with Odd Values in a Matrix.
    # 31.2 MB, less than 5.50% of Python3 online submissions for Cells with Odd Values in a Matrix.
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        import numpy as np
        ans = np.zeros(shape=(m, n))
        for idx in indices:
            row, col = idx
            ans[row] += 1
            ans[:,col] +=1
        ans  = ans % 2
        return int(ans.sum())


if __name__ == "__main__":
    so = Solution()
    print(so.oddCells(48, 37, [[40,5]]))