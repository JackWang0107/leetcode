import collections
from typing import *
class Solution:
    # 24 ms, faster than 99.08% of Python3 online submissions for Unique Number of Occurrences.
    # 14.4 MB, less than 64.26% of Python3 online submissions for Unique Number of Occurrences.
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        from collections import Counter
        time = Counter(arr)
        return len(set(time.values())) == len(time.values())


if __name__ == "__main__":
    so = Solution()
    print(so.uniqueOccurrences(arr = [-3,0,1,-3,1,1,1,-3,10,0]))
