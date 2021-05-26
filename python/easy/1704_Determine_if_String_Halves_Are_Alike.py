from typing import *
class Solution:
    # 40 ms, faster than 18.31% of Python3 online submissions for Determine if String Halves Are Alike.
    # 14.4 MB, less than 36.03% of Python3 online submissions for Determine if String Halves Are Alike.
    def halvesAreAlike(self, s: str) -> bool:
        left, right = 0, 0
        vowels = list("aeiou")
        for i in range(len(s)//2):
            if s[i].lower() in vowels:
                left += 1
        for i in range(len(s)//2, len(s)):
            if s[i].lower() in vowels:
                right += 1
        return right == left

if __name__ == "__main__":
    so = Solution()
    print(so.halvesAreAlike("aaeeqq"))