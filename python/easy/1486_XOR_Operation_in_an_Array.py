from typing import *
class Solution:
    # 28 ms, faster than 80.97% of Python3 online submissions for XOR Operation in an Array.
    # 14.2 MB, less than 50.73% of Python3 online submissions for XOR Operation in an Array.
    def xorOperation(self, n: int, start: int) -> int:
        ans = 0
        for i in range(n):
            ans = ans ^ ( start + 2 * i )
        return ans

    # 32 ms, faster than 53.95% of Python3 online submissions for XOR Operation in an Array.
    # 14.1 MB, less than 92.57% of Python3 online submissions for XOR Operation in an Array.
    def xorOperation(self, n: int, start: int) -> int:
        from functools import reduce
        from operator import xor
        return reduce(xor, (start+2*i for i in range(n)))

if __name__ == "__main__":
    so = Solution()
    print(so.xorOperation(n = 1, start = 7))
