from typing import *
class Solution:
    # 112 ms, faster than 40.40% of Python3 online submissions for The K Weakest Rows in a Matrix.
    # 14.4 MB, less than 90.91% of Python3 online submissions for The K Weakest Rows in a Matrix.
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        strength = [ (idx*0.001+sum(row),idx) for idx, row in enumerate(mat) ]
        strength.sort(key=lambda x:x[0])
        return [row[1] for row in strength[:k]]


if __name__ == "__main__":
    so = Solution()
    print(so.kWeakestRows(mat = 
[[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]], 
k = 2))