from typing import *
class Solution:
    # 36 ms, faster than 38.77% of Python3 online submissions for Number of Good Pairs
    # 14.3 MB, less than 41.67% of Python3 online submissions for Number of Good Pairs
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ans = 0
        for idx1, num1 in enumerate(nums[:-1]):
            for idx2,num2 in enumerate(nums[idx1+1:]):
                if num1 == num2:
                    ans+=1
        return ans

    #  28 ms, faster than 90.91% of Python3 online submissions for Number of Good Pairs
    # 14.2 MB, less than 41.67% of Python3 online submissions for Number of Good Pairs.
    def numIdenticalPairs(self, nums: List[int]) -> int:
        from collections import defaultdict
        numCount = defaultdict(int)
        for x in nums:
            numCount[x] += 1
        ans = 0
        for count in numCount.values():
            if count >= 2:
                ans += (count * (count-1)) // 2
        return ans

if __name__ == "__main__":
    so = Solution()
    print(so.numIdenticalPairs([1,1,1,1]))