from typing import *
class Solution:
    # 60 ms, faster than 76.33% of Python3 online submissions for Increasing Decreasing String.
    # 14 MB, less than 99.00% of Python3 online submissions for Increasing Decreasing String.
    def sortString(self, s: str) -> str:
        from collections import Counter
        available_len = len(s)
        letter_dict = dict(Counter(sorted(s)))
        letters = list(letter_dict.keys())
        ans = ""
        while available_len > 0:
            for i in [1, -1]:
                for letter in letters[::i]:
                    if letter_dict[letter] > 0:
                        ans += letter
                        letter_dict[letter] -= 1
                        available_len -= 1
        return ans

if __name__ == "__main__":
    so = Solution()
    print(so.sortString(s = "spo"))