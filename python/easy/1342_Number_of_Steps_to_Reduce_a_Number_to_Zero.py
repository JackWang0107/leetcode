from typing import *
class Solution:
    # 32 ms, faster than 53.97% of Python3 online submissions for Number of Steps to Reduce a Number to Zero.
    # 14.2 MB, less than 35.20% of Python3 online submissions for Number of Steps to Reduce a Number to Zero.
    def numberOfSteps(self, num: int) -> int:
        ans = 0
        while num != 0:
            if num & 1:
                num -= 1
            else:
                num = int(num/2 )
            ans += 1
        return ans

    #  20 ms, faster than 98.79% of Python3 online submissions for Number of Steps to Reduce a Number to Zero.
    # 14.3 MB, less than 35.20% of Python3 online submissions for Number of Steps to Reduce a Number to Zer
    def numberOfSteps(self, num: int) -> int:
        def rec(num):
            if num == 0 or num == 1:
                return num
            elif num % 2:
                return 2 + rec(num // 2)
            else:
                return 1 + rec(num // 2)
        return rec(num)



if __name__ == "__main__":
    so = Solution()
    print(so.numberOfSteps(123))