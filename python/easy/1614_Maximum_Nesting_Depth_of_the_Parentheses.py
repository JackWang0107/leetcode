from typing import *
class Solution:
    # 32 ms, faster than 54.06% of Python3 online submissions for Maximum Nesting Depth of the Parentheses.
    # 14 MB, less than 90.08% of Python3 online submissions for Maximum Nesting Depth of the Parentheses.
    def maxDepth(self, s: str) -> int:
        max_depth = 0
        temp = 0
        for letter in s:
            if letter == "(":
                temp += 1
            if max_depth <= temp:
                max_depth = temp
            if letter == ")":
                temp -= 1
        return max_depth

if __name__ == "__main__":
    so = Solution()
    print(so.maxDepth("1+(2*3)/(2-1)"))