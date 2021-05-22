from typing import *
class Solution:
    # 24 ms, faster than 93.63% of Python3 online submissions for Count of Matches in Tournament.
    # 14 MB, less than 88.59% of Python3 online submissions for Count of Matches in Tournament.
    def numberOfMatches(self, n: int) -> int:
        total = 0
        while n > 1:
            if n%2 == 1:
                total += n//2
                n = (n+1)/2
                continue
            total += n/2
            n = n/2
        return int(total)

    # simple math ^-^
    def numberOfMatches(self, n: int) -> int:
        return n-1

if __name__ == "__main__":
    so = Solution()
    print(so.numberOfMatches(n=7))