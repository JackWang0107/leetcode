from typing import *
class Solution:
    # 20 ms, faster than 99.41% of Python3 online submissions for Longer Contiguous Segments of Ones than Zeros.
    # 14.1 MB, less than 90.93% of Python3 online submissions for Longer Contiguous Segments of Ones than Zeros.
    def checkZeroOnes(self, s: str) -> bool:
        max_0_length = 0
        temp_0_length = 0
        max_1_length = 0
        temp_1_length = 0
        last = -1
        for digit in s:
            if digit == "1":
                if max_0_length < temp_0_length:
                    max_0_length = temp_0_length
                temp_0_length = 0
                temp_1_length += 1
            if digit == "0":
                if max_1_length < temp_1_length:
                    max_1_length = temp_1_length
                temp_1_length = 0
                temp_0_length += 1
            if max_0_length < temp_0_length:
                max_0_length = temp_0_length
            if max_1_length < temp_1_length:
                max_1_length = temp_1_length
        return max_0_length < max_1_length


if __name__ == "__main__":
    so = Solution()
    print(so.checkZeroOnes("110100010"))

