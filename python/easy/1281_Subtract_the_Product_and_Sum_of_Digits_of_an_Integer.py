from typing import *

# 28 ms, faster than 78.37% of Python3 online submissions for Subtract the Product and Sum of Digits of an Integer.
# 14.3 MB, less than 42.94% of Python3 online submissions for Subtract the Product and Sum of Digits of an Integer.
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digits = self.get_digits(n)
        product = 1
        for digit in digits:
            product *= digit
        return product - sum(digits)

    def get_digits(self, n:int) -> List[int]:
        ans = []
        while(n>0):
            ans.append(n%10)
            n = n // 10
        return ans

# 32 ms, faster than 49.63% of Python3 online submissions for Subtract the Product and Sum of Digits of an Integer.
# 14.1 MB, less than 89.67% of Python3 online submissions for Subtract the Product and Sum of Digits of an Integer.
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        add=0
        product=1
        n=str(n)
        for i in n:
            add+=int(i)
            product=product*int(i)
        ans=product-add
        return ans
    
    #  32 ms, faster than 49.63% of Python3 online submissions for Subtract the Product and Sum of Digits of an Integer.
    # 14.1 MB, less than 70.45% of Python3 online submissions for Subtract the Product and Sum of Digits of an Integer.
    def subtractProductAndSum(self, n: int) -> int:
        sum_n = 0
        product_n = 1
        while n >0 :
            temp_digit = n % 10
            sum_n += temp_digit
            product_n *= temp_digit
            n = n // 10
        return product_n - sum_n

if __name__ == "__main__":
    so = Solution()
    print( so.subtractProductAndSum(4421) )