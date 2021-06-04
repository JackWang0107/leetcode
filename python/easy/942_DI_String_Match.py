from typing import *
class Solution:
    # 6308 ms, faster than 5.02% of Python3 online submissions for DI String Match.
    # 15.5 MB, less than 6.53% of Python3 online submissions for DI String Match.
    def diStringMatch(self, s: str) -> List[int]:
        ans = []
        rangelist = [i for i in range(0,len(s)+1)]
        for char in s:
            if char=='I':
                ans.append(min(rangelist))
                rangelist.remove(min(rangelist))
            else:
                ans.append(max(rangelist))
                rangelist.remove(max(rangelist))
        ans.extend(rangelist) #appending last element left int he rangelist
        return ans

    # 60 ms, faster than 83.53% of Python3 online submissions for DI String Match.
    # 15 MB, less than 99.00% of Python3 online submissions for DI String Match.
    def diStringMatch(self, s: str) -> List[int]:
        head = 0
        tail = len(s)
        ans = []
        for letter in s:
            if letter == "D":
                ans.append(tail)
                tail -= 1
            if letter == "I":
                ans.append(head)
                head += 1
        if head == tail:
            ans.append(head)
        return ans



if __name__ == "__main__":
    so = Solution()
    print(so.diStringMatch(s = "DDI"))