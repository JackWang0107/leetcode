from typing import *
class Solution:
    # 40 ms, faster than 99.25% of Python3 online submissions for Final Prices With a Special Discount in a Shop.
    # 14.1 MB, less than 98.63% of Python3 online submissions for Final Prices With a Special Discount in a Shop.
    def finalPrices(self, prices: List[int]) -> List[int]:
        ans = []
        for i in range(len(prices)):
            flag = 0
            for j in range(i+1, len(prices)):
                if prices[j] <= prices[i]:
                    flag = 1
                    ans.append(prices[i] - prices[j])
                    break
            if flag == 0:
                ans.append(prices[i])
        return ans


if __name__ == "__main__":
    so = Solution()
    print(so.finalPrices(prices = [8,4,6,2,3]))