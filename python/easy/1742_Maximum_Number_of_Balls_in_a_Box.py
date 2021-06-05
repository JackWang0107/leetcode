from typing import *
class Solution:
    # 736 ms, faster than 29.02% of Python3 online submissions for Maximum Number of Balls in a Box.
    # 14 MB, less than 94.03% of Python3 online submissions for Maximum Number of Balls in a Box.
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        ans = {}
        for ball in range(lowLimit, highLimit+1):
            try:
                key = sum(int(digit) for digit in str(ball))
                ans[key]  += 1
            except KeyError:
                ans[key] = 1
        return max(ans.values())

    # 356 ms, faster than 96.80% of Python3 online submissions for Maximum Number of Balls in a Box.
    # 14.1 MB, less than 81.86% of Python3 online submissions for Maximum Number of Balls in a Box.
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        ans = {}
        for ball in range(lowLimit, highLimit+1):
            key = 0
            while ball > 0:
                key += ball % 10
                ball //= 10
            try:
                ans[key]  += 1
            except KeyError:
                ans[key] = 1
        return max(ans.values())


if __name__ == "__main__":
    so = Solution()
    print(so.countBalls(lowLimit = 19, highLimit = 28))