from typing import *
class Solution:
    # 36 ms, faster than 55.50% of Python3 online submissions for Reverse Words in a String III.
    # 14.6 MB, less than 86.02% of Python3 online submissions for Reverse Words in a String III.
    def reverseWords(self, s: str) -> str:
        return " ".join([word[::-1] for word in s.split(" ")])

    # 44 ms, faster than 27.30% of Python3 online submissions for Reverse Words in a String III.
    # 14.7 MB, less than 72.06% of Python3 online submissions for Reverse Words in a String III.
    def reverseWords(self, s: str) -> str:
        ans = ""
        words = s.split(" ")
        for word in words[:-1]:
            ans+= word[::-1]+" "
        return ans+words[-1][::-1]

if __name__ == "__main__":
    so = Solution()
    print(so.reverseWords(s = "Let's take LeetCode contest"))