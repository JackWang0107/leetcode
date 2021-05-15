from typing import *
class Solution:
    # 60 ms, faster than 61.39% of Python3 online submissions for Shuffle the Array.
    # 14.2 MB, less than 98.76% of Python3 online submissions for Shuffle the Array.
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = []
        for i in range(n):
            ans.append(nums[i])
            ans.append(nums[n + i])
        return ans

    # 56 ms, faster than 84.56% of Python3 online submissions for Shuffle the Array.
    # 14.2 MB, less than 98.76% of Python3 online submissions for Shuffle the Array.
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = []
        for x, y in zip(nums[:n], nums[n:]):
            ans.append(x)
            ans.append(y)
        return ans

    #  60 ms, faster than 61.39% of Python3 online submissions for Shuffle the Array.
    # 14.5 MB, less than 49.20% of Python3 online submissions for Shuffle the Array.
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        left = nums[:n]
        right = nums[n:]

        ans = [ None ]* (n *2)
        ans[::2] = left
        ans[1::2] = right
        return ans

    # 60 ms, faster than 61.39% of Python3 online submissions for Shuffle the Array.
    # 14.5 MB, less than 49.20% of Python3 online submissions for Shuffle the Array.
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = [ None ] * ( n* 2)
        ans[::2] = nums[:n]
        ans[1::2] = nums[n:]
        return ans


if __name__ == "__main__":
    so = Solution()
    print(so.shuffle(nums = [2,5,1,3,4,7], n = 3))