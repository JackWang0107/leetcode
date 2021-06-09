from typing import *
class Solution:
    # 192 ms, faster than 79.07% of Python3 online submissions for Reverse String.
    # 18.4 MB, less than 97.20% of Python3 online submissions for Reverse String.
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s = s.reverse()


if __name__ == "__main__":
    s = ["h","e","l","l","o"]
    so = Solution()
    so.reverseString(s)
    print(s)