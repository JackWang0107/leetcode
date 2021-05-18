from typing import *
class Solution:
    # 68 ms, faster than 48.78% of Python3 online submissions for Decompress Run-Length Encoded List.
    # 14.8 MB, less than 24.68% of Python3 online submissions for Decompress Run-Length Encoded List.
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        ans = []
        for freq, val in zip(nums[::2], nums[1::2]):
            ans.extend([val]*freq)
        return ans

    # 64 ms, faster than 77.17% of Python3 online submissions for Decompress Run-Length Encoded List
    # 15 MB, less than 24.68% of Python3 online submissions for Decompress Run-Length Encoded List.
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        from itertools import chain
        return list(chain(*[[val]*freq for freq, val in zip(nums[::2], nums[1::2])]))

    
if __name__ == "__main__":
    so = Solution()
    print(so.decompressRLElist(nums = [1,1,2,3]))