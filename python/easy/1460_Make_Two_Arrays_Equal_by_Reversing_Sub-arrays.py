from typing import *
class Solution:
    # 84 ms, faster than 25.19% of Python3 online submissions for Make Two Arrays Equal by Reversing Sub-arrays.
    # 14.5 MB, less than 31.19% of Python3 online submissions for Make Two Arrays Equal by Reversing Sub-arrays.
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        from collections import Counter
        counter_tar = Counter(target)
        counter_arr = Counter(arr)
        return len(target) == len(arr) and  not (set(counter_arr.items())-set(counter_tar.items()))


if __name__ == "__main__":
    so = Solution()
    print(so.canBeEqual([1,2,2,3],[1,1,2,3]))

