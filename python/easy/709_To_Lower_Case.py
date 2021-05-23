from typing import *
class Solution:
    # 20 ms, faster than 98.02% of Python3 online submissions for To Lower Case.
    # 14.3 MB, less than 33.22% of Python3 online submissions for To Lower Case.
    def toLowerCase(self, s: str) -> str:
        s = list(s)
        for idx, letter in enumerate(s):
            s[idx] = letter.lower()
        return "".join(s)

    # 24 ms, faster than 91.99% of Python3 online submissions for To Lower Case.
    # 14.1 MB, less than 86.86% of Python3 online submissions for To Lower Case.
    def toLowerCase(self, s: str) -> str:
        return s.lower()


if __name__ == "__main__":
    so = Solution()
    print(so.toLowerCase("Hello"))