from typing import *
class Solution:
    # 272 ms, faster than 29.84% of Python3 online submissions for Count the Number of Consistent Strings.
    # 16.3 MB, less than 12.74% of Python3 online submissions for Count the Number of Consistent Strings.
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        return sum([set(allowed).issuperset(word) for word in words])

    # 224 ms, faster than 78.63% of Python3 online submissions for Count the Number of Consistent Strings.
    # 16 MB, less than 74.39% of Python3 online submissions for Count the Number of Consistent Strings.
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        sums = 0
        for word in words:
            if set(word).issubset(allowed):
                sums += 1
        return sums

    # 204 ms, faster than 99.52% of Python3 online submissions for Count the Number of Consistent Strings.
    # 16 MB, less than 92.01% of Python3 online submissions for Count the Number of Consistent Strings.
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        for word in words:
            for letter in word:
                if letter not in allowed:
                    count += 1
                    break

if __name__ == "__main__":
    so = Solution()
    print(so.countConsistentStrings(allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"]))