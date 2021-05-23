from abc import abstractproperty
from typing import *

class Solution:
    # 32 ms, faster than 67.00% of Python3 online submissions for Replace All Digits with Characters
    # 14.2 MB, less than 72.66% of Python3 online submissions for Replace All Digits with Characters.
    def replaceDigits(self, s: str) -> str:
        def shift(c:str, x:str):
            alphabet = "abcdefghijklmnopqrstuvwxyz"
            return alphabet[alphabet.index(c) + int(x)]

        s = list(s)
        idx = 1
        while idx < len(s):
            s[idx] = shift(s[idx-1], s[idx])
            idx += 2
        return "".join(s)
    
    # 32 ms, faster than 67.00% of Python3 online submissions for Replace All Digits with Characters.
    # 14.3 MB, less than 43.09% of Python3 online submissions for Replace All Digits with Characters.
    def replaceDigits(self, s: str) -> str:
        ans = []
        for idx, value in enumerate(s):
            if idx%2 != 0:
                ans.append(chr(ord(ans[-1]) + int(value)))
                continue
            ans.append(value)
        return "".join(ans)

if __name__ =="__main__":
    so = Solution()
    print(so.replaceDigits(s = "a1c1e1"))