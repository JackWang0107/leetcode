from typing import *
class Solution:
    #  56 ms, faster than 53.14% of Python3 online submissions for Shuffle String.
    # 14.2 MB, less than 52.25% of Python3 online submissions for Shuffle String.
    def restoreString(self, s: str, indices: List[int]) -> str:
        ans = " "*len(indices)
        for letter, idx in zip(s, indices):
            ans = ans[ : idx ] + letter + ans[idx+1 :]
        return ans

    # 48 ms, faster than 92.94% of Python3 online submissions for Shuffle String.
    # 14.3 MB, less than 52.25% of Python3 online submissions for Shuffle String.
    def restoreString(self, s: str, indices: List[int]) -> str:
        ans = [" "]*len(indices)
        for letter, idx in zip(s, indices):
            ans[idx] = letter
        return "".join(ans)

    # 48 ms, faster than 92.94% of Python3 online submissions for Shuffle String.
    # 14.3 MB, less than 19.23% of Python3 online submissions for Shuffle String.
    def restoreString(self, s: str, indices: List[int]) -> str:
        ans = ['a' for i in indices ]
        for c, index, in zip(s, indices):
            ans[index] = c
        return  "".join(ans)
    
    # 48 ms, faster than 92.94% of Python3 online submissions for Shuffle String
    # 14.1 MB, less than 78.32% of Python3 online submissions for Shuffle String.
    def restoreString(self, s: str, indices: List[int]) -> str:
        kek=[None] * len(s)
        for i, letter in zip(indices, s):
            kek[i] = letter
        return ''.join(kek)

    # 48 ms, faster than 92.94% of Python3 online submissions for Shuffle String.
    # 14.2 MB, less than 52.25% of Python3 online submissions for Shuffle String.
    def restoreString(self, s: str, indices: List[int]) -> str:
        ans = ['a' for i in indices ]
        for letter, index, in zip(s, indices):
            ans[index] = letter
        
        final = ""
        for letter in ans:
            final += letter
        return  final



if __name__ == "__main__":
    so = Solution()
    print(so.restoreString("codeleet", indices = [4,5,6,7,0,2,1,3]))