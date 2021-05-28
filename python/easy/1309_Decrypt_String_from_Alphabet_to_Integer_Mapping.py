from typing import *
class Solution:
    # 32 ms, faster than 57.50% of Python3 online submissions for Decrypt String from Alphabet to Integer Mapping.
    # 14.1 MB, less than 76.00% of Python3 online submissions for Decrypt String from Alphabet to Integer Mapping.
    def freqAlphabets(self, s: str) -> str:
        ans = []
        temp = ""
        for letter in s:
            if letter != "#":
                temp += letter
            else:
                ans.extend(list(temp[:-2]))
                ans.append(temp[-2:])
                temp = ""
        ans.extend(temp)
        return "".join(map(lambda x:chr(int(x)+ord("a") - 1), ans))

    
    # 32 ms, faster than 57.50% of Python3 online submissions for Decrypt String from Alphabet to Integer Mapping.
    # 14 MB, less than 91.25% of Python3 online submissions for Decrypt String from Alphabet to Integer Mapping.
    def freqAlphabets(self, s: str) -> str:
        ans = ""
        i = len(s)-1
        while i>=0:
            if s[i]=="#":
                ans = ans + chr(int(s[i-2:i])+96)
                i=i-2
            else:
                ans = ans + chr(int(s[i])+96)
            i -= 1
        return ans[::-1]



if __name__ == "__main__":
    so = Solution()
    print(so.freqAlphabets(s = "12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"))