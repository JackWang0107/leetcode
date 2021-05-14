from typing import *
class Solution:
    # 56 ms, faster than 37.89% of Python3 online submissions for Richest Customer Wealth.
    # 14 MB, less than 94.46% of Python3 online submissions for Richest Customer Wealth
    def maximumWealth(self, accounts:List[List[int]]) -> int:
        max = -1
        for i in range(len(accounts)):
            tmp = sum(accounts[i])
            if max <= tmp:
                max = tmp
        return max
    
    # 40 ms, faster than 99.77% of Python3 online submissions for Richest Customer Wealth
    # 14.5 MB, less than 26.79% of Python3 online submissions for Richest Customer Wealth
    def maximumWealth(self, accounts:List[List[int]]) -> int:
        return max([ sum(account) for account in accounts])



if __name__ == "__main__":
    so = Solution()
    print(so.maximumWealth( [[2,8,7],[7,1,3],[1,9,5]]))
