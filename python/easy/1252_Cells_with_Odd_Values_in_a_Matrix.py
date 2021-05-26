from typing import *
class Solution:
    # simple but expansive numpy solution
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

    # Counting number of odd-number cells can be tranformed to counting non-zero cells by % 2
    # so here we let values of each cell are 0 or 1
    # then for a m*n matrix, the number of non-zero cells can be calculated by a*m+b*n - 2*a*b
    # where a is column number and b is row number, and we need to substract overlap
    # 40 ms, faster than 84.11% of Python3 online submissions for Cells with Odd Values in a Matrix.
    # 14 MB, less than 97.56% of Python3 online submissions for Cells with Odd Values in a Matrix
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        from collections import Counter
        x = 0
        y = 0
        for i in dict(Counter([x[0] for x in indices])).values():
            if i % 2 == 1:
                x += 1
        for j in dict(Counter([x[1] for x in indices])).values():
            if j % 2 == 1:
                y += 1
        return x * n + y *m - x* y*2

if __name__ == "__main__":
    so = Solution()
    print(so.oddCells(m = 2, n = 3, indices = [[0,1],[1,1]]))