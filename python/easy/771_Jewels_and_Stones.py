from typing import *
class Solution:
    # 32 ms, faster than 53.65% of Python3 online submissions for Jewels and Stones.
    # 14.1 MB, less than 90.99% of Python3 online submissions for Jewels and Stones.
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        num = 0
        for letter in jewels:
            while (idx:=stones.find(letter)) != -1:
                num += 1
                stones = stones[:idx]+stones[idx+1:]
        return num

    # 24 ms, faster than 95.07% of Python3 online submissions for Jewels and Stones
    # 14.2 MB, less than 45.09% of Python3 online submissions for Jewels and Stones.
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum ( stones.count(letter) for letter in jewels)


if __name__ == "__main__":
    so = Solution()
    print(so.numJewelsInStones( jewels = "bcd", stones = "cba"))