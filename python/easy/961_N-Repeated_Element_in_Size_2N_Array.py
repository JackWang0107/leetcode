from typing import *
class Solution:
    # 204 ms, faster than 60.02% of Python3 online submissions for N-Repeated Element in Size 2N Array.
    # 15.8 MB, less than 11.73% of Python3 online submissions for N-Repeated Element in Size 2N Array.
    def repeatedNTimes(self, nums: List[int]) -> int:
        from collections import Counter
        ans =  dict(Counter(nums))
        for num, time in ans.items():
            if time >= 2:
                return num

    # 192 ms, faster than 92.89% of Python3 online submissions for N-Repeated Element in Size 2N Array.
    # 15.6 MB, less than 34.42% of Python3 online submissions for N-Repeated Element in Size 2N Array.
    def repeatedNTimes(self, nums: List[int]) -> int:
        nums_copy = []
        for num in nums:
            if num in nums_copy:
                return num
            else:
                nums_copy.append(num)

    # 184 ms, faster than 99.33% of Python3 online submissions for N-Repeated Element in Size 2N Array.
    # 15.5 MB, less than 66.30% of Python3 online submissions for N-Repeated Element in Size 2N Array.
    def repeatedNTimes(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                return i

if __name__ == "__main__":
    so = Solution()
    print(so.repeatedNTimes([2,1,2,5,3,2]))