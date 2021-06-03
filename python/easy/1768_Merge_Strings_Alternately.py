from typing import *
class Solution:
    # 40 ms, faster than 7.35% of Python3 online submissions for Merge Strings Alternately.
    # 14.1 MB, less than 76.49% of Python3 online submissions for Merge Strings Alternately.
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = []
        for idx in range(min(len(word1), len(word2))):
            ans.append(word1[idx])
            ans.append(word2[idx])
        if idx < len(word2)-1:
            ans.append(word2[idx+1:])
        else:
            ans.append(word1[idx+1:])
        return "".join(ans)


if __name__ == "__main__":
    so = Solution()
    print(so.mergeAlternately(word1 = "abcd", word2 = "pq"))