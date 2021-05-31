from typing import*
class Solution:
    # 52 ms, faster than 49.33% of Python3 online submissions for Self Dividing Numbers.
    # 14.2 MB, less than 53.90% of Python3 online submissions for Self Dividing Numbers.
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []
        for i in range(left, right+1):
            for digit in map(lambda x:int(x), str(i)):
                flag = 0
                try:
                    if i % digit != 0:
                        break
                except ZeroDivisionError:
                    break
                flag = 1
            if flag == 1:
                ans.append(i)
        return ans
                

if __name__ == "__main__":
    so = Solution()
    print(so.selfDividingNumbers(left = 1, right = 22))