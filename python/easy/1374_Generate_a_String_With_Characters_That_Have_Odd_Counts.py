from typing import *
class Solution:
    # 28 ms, faster than 77.62% of Python3 online submissions for Generate a String With Characters That Have Odd Counts.
    # 14.2 MB, less than 63.03% of Python3 online submissions for Generate a String With Characters That Have Odd Counts.
    def generateTheString(self, n: int) -> str:
        flag = 0
        if n % 2 == 0:
            flag =1
        return "a"*(n-flag) + "b" * flag

    # 20 ms, faster than 98.91% of Python3 online submissions for Generate a String With Characters That Have Odd Counts.
    # 14.1 MB, less than 63.03% of Python3 online submissions for Generate a String With Characters That Have Odd Counts.
    def generateTheString(self, n: int) -> str:
        if n % 2 != 0:
            return "a"*n
        return "a" * (n-1) + "b"


if __name__ == "__main__":
    so = Solution()
    print(so.generateTheString(5))