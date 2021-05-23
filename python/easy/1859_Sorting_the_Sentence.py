from types import WrapperDescriptorType
from typing import *
class Solution:
    # 32 ms, faster than 68.12% of Python3 online submissions for Sorting the Sentence.
    # 14.1 MB, less than 76.21% of Python3 online submissions for Sorting the Sentence.
    def sortSentence(self, s: str) -> str:
        ans = [None] * len(s.split(" "))
        for word in s.split(" "):
            # find idx manually
            idx = -1
            while ascii('0') <= word[idx] <= ascii("9"):
                idx -= 1
            value, idx = word[:idx], int(word[idx:])
            ans[idx-1] = value
        return " ".join(ans)

    # 32 ms, faster than 68.12% of Python3 online submissions for Sorting the Sentence.
    #  14.2 MB, less than 47.34% of Python3 online submissions for Sorting the Sentence.
    def sortSentence(self, s: str) -> str:
        ans = [None] * len(s.split(" "))
        for word in s.split(" "):
            ans[ int(word[-1])-1 ] = word[:-1]
        return " ".join(ans)

    # 28 ms, faster than 86.91% of Python3 online submissions for Sorting the Sentence.
    # 14.2 MB, less than 76.21% of Python3 online submissions for Sorting the Sentence.
    def sortSentence(self, s: str) -> str:
        # very pythonic, by using lambda
        return " ".join([ word[:-1] for word in sorted( s.split(), key=lambda x:x[-1] ) ])



if __name__ == "__main__":
    so = Solution()
    print(so.sortSentence(s = "is2 sentence4 This1 a3"))