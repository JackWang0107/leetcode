from typing import *
class Solution:
    # 28 ms, faster than 76.26% of Python3 online submissions for Maximum 69 Number.
    # 14.1 MB, less than 68.38% of Python3 online submissions for Maximum 69 Number.
    def maximum69Number (self, num: int) -> int:
        num = str(num)
        for i in range(len(num)):
            if num[i] == "6":
                return int(num[:i] + "9" + num[i+1:] )
        return int(num)
    
    def maximum69Number (self, num: int) -> int:
        # 28 ms, faster than 76.26% of Python3 online submissions for Maximum 69 Number.
        # 14.1 MB, less than 89.39% of Python3 online submissions for Maximum 69 Number.
        return int(str(num).replace("6", "9", 1))


if __name__ == "__main__":
    so = Solution()
    print(so.maximum69Number(99699))