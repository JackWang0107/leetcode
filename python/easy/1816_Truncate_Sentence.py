from typing import *
class Solution:
    # 24 ms, faster than 95.32% of Python3 online submissions for Truncate Sentence.
    # 14 MB, less than 99.13% of Python3 online submissions for Truncate Sentence.
    def truncateSentence(self, s: str, k: int) -> str:
        return " ".join(s.split(" ")[:k])


if __name__ == "__main__":
    so = Solution()
    print(so.truncateSentence(s = "Hello how are you Contestant", k = 4))
