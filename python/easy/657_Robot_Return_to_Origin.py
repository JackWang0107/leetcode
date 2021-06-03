from typing import *
class Solution:
    # 32 ms, faster than 94.89% of Python3 online submissions for Robot Return to Origin.
    # 14.5 MB, less than 19.93% of Python3 online submissions for Robot Return to Origin.
    def judgeCircle(self, moves: str) -> bool:
        ans = {move:moves.count(move) for move in "RLUD"}
        return ans["R"] == ans["L"] and ans["U"] == ans["D"]


if __name__ == "__main__":
    so = Solution()
    print(so.judgeCircle(moves = "UDL"))