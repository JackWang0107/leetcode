from typing import *
class Solution:
    # 28 ms, faster than 81.66% of Python3 online submissions for Split a String in Balanced Strings.
    # 14.2 MB, less than 69.96% of Python3 online submissions for Split a String in Balanced Strings
    def balancedStringSplit(self, s: str) -> int:
        ans = 0
        idx = 0
        total_go_through = 0
        while total_go_through < len(s) and idx < len(s)-1:
            sub_len = 2
            while s[idx:idx+sub_len].count("L") != s[idx:idx+sub_len].count("R") and total_go_through < len(s):
                sub_len += 2
                total_go_through = idx + sub_len
            idx += sub_len
            ans += 1
        return ans

    # 32 ms, faster than 54.83% of Python3 online submissions for Split a String in Balanced Strings.
    # 14.1 MB, less than 69.96% of Python3 online submissions for Split a String in Balanced Strings.
    def balancedStringSplit(self, s: str) -> int:
        count_L, count_R, ans = 0, 0, 0
        for i in s:
            if i == "R":
                count_R += 1
            else:
                count_L += 1
            if count_R == count_L:
                ans += 1
        return ans


if __name__ == "__main__":
    so =Solution()
    print(so.balancedStringSplit(s = "RLRRLLRLRL"))