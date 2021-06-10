from typing import *
class Solution:
    # 172 ms, faster than 58.41% of Python3 online submissions for Delete Columns to Make Sorted.
    # 14.8 MB, less than 58.02% of Python3 online submissions for Delete Columns to Make Sorted.
    def minDeletionSize(self, strs: List[str]) -> int:
        nums = 0
        for i in range(len(strs[0])):
            k = 0
            for s in strs[1:]:
                last = strs[k]
                if s[i] >= last[i]:
                    k+=1
                else:
                    nums+=1
                    break
        return nums


if __name__ == "__main__":
    so = Solution()
    print(so.minDeletionSize(strs = ["zyx","wvu","tsr"]))
