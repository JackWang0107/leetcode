from typing import List


class Solution:
    # 52ms, 
    def runningSum(self, nums:List[int]) -> List[int]:
        return [ sum(nums[:i+1]) for i in range(len(nums)) ]
    
    # 
    def runningSum(self, nums:List[int]) -> List[int]:
        ans: List[int] = []
        temp = 0
        for i in nums:
            temp += i
            ans.append(temp)
        return ans

if __name__ == "__main__":
    so = Solution()
    print(so.runningSum(nums=[1, 2, 3, 4]))