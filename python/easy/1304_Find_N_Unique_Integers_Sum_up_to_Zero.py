from typing import *
class Solution:
    #  24 ms, faster than 98.52% of Python3 online submissions for Find N Unique Integers Sum up to Zero.
    # 14.2 MB, less than 91.76% of Python3 online submissions for Find N Unique Integers Sum up to Zero.
    def sumZero(self, n: int) -> List[int]:
        ans = []
        if n % 2 == 1:
            ans = [0]
        for i in range(1, n//2+1):
            ans.append(i)
            ans.append(-i)
        return ans

    #  20 ms, faster than 99.71% of Python3 online submissions for Find N Unique Integers Sum up to Zero.
    # 14.2 MB, less than 91.76% of Python3 online submissions for Find N Unique Integers Sum up to Zero.
    def sumZero(self, n: int) -> List[int]:
        result = [x for i in range(1, n//2+1) for x in {i, -i}]
        if n % 2:
            result.append(0)
        return result


if __name__ == "__main__":
    so = Solution()
    print(so.sumZero(5))
