from typing import *
class Solution:
    # 220 ms, faster than 87.86% of Python3 online submissions for Decode XORed Array.
    # 15.9 MB, less than 14.87% of Python3 online submissions for Decode XORed Array.
    def decode(self, encoded: List[int], first: int) -> List[int]:
        ans = [ first ]
        for item in encoded:
            ans.append(ans[-1]^item)
        return ans

if __name__ == "__main__":
    so = Solution()
    print(so.decode(encoded = [6,2,7,3], first = 4))