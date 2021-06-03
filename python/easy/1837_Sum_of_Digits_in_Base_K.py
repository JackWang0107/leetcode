from typing import *
class Solution:
    # 28 ms, faster than 84.42% of Python3 online submissions for Sum of Digits in Base K.
    # 14.2 MB, less than 46.12% of Python3 online submissions for Sum of Digits in Base K.
    def sumBase(self, n: int, k: int) -> int:
        ans = []
        while n > 0:
            ans.append(n%k)
            n = n//k
        return sum(ans)

    # 28 ms, faster than 84.42% of Python3 online submissions for Sum of Digits in Base K.
    # 14 MB, less than 98.07% of Python3 online submissions for Sum of Digits in Base K.
    def sumBase(self, n: int, k: int) -> int:
        ans = 0
        while n > 0:
            ans+=n%k
            n = n//k
        return ans

if __name__ == "__main__":
    so = Solution()
    print(so.sumBase(34, 6))