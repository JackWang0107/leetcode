from typing import *
class Solution:
    # 128 ms, faster than 7.81% of Python3 online submissions for Sort Integers by The Number of 1 Bits.
    # 14.5 MB, less than 43.57% of Python3 online submissions for Sort Integers by The Number of 1 Bits.
    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr, key=lambda x:bin(x).count("1")+x/max(arr))


if __name__ == "__main__":
    so = Solution()
    print(so.sortByBits([1024,512,256,128,64,32,16,8,4,2,1]))