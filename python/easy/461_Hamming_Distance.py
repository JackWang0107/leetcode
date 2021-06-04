from typing import *
class Solution:
    # 28 ms, faster than 82.15% of Python3 online submissions for Hamming Distance.
    # 14.1 MB, less than 90.58% of Python3 online submissions for Hamming Distance.
    def hammingDistance(self, x: int, y: int) -> int:
        return str(bin(x^y)).count("1")

    # 28 ms, faster than 82.15% of Python3 online submissions for Hamming Distance
    # 14.3 MB, less than 43.56% of Python3 online submissions for Hamming Distance.
    def hammingDistance(self, x: int, y: int) -> int:
        return sum(1 for i in bin(x^y) if i == "1")


if __name__ == "__main__":
    so = Solution()
    print(so.hammingDistance(3, 1))