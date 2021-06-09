from typing import *
class Solution:
    # 72 ms, faster than 97.12% of Python3 online submissions for Counting Bits.
    # 20.8 MB, less than 71.37% of Python3 online submissions for Counting Bits.
    def countBits(self, n: int) -> List[int]:
        return [bin(n).count("1") for n in range(n+1)]


if __name__ == "__main__":
    so = Solution()
    print(so.countBits(n=5))