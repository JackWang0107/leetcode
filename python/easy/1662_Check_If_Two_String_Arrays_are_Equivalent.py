from typing import *
class Solution:
    # 32 ms, faster than 59.20% of Python3 online submissions for Check If Two String Arrays are Equivalent.
    # 14.2 MB, less than 60.51% of Python3 online submissions for Check If Two String Arrays are Equivalent
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        if "".join(word1) == "".join(word2):
            return True
        return False

    # 24 ms, faster than 95.62% of Python3 online submissions for Check If Two String Arrays are Equivalent.
    # 14.5 MB, less than 31.72% of Python3 online submissions for Check If Two String Arrays are Equivalent
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return "".join(word1) == "".join(word2)

if __name__ == "__main__":
    so = Solution()
    print(so.arrayStringsAreEqual(word1 = ["a", "bc"], word2 = ["ab", "c"]))