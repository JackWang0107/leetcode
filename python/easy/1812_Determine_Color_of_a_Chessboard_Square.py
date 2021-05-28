from typing import *
class Solution:
    # 24 ms, faster than 95.47% of Python3 online submissions for Determine Color of a Chessboard Square.
    # 13.9 MB, less than 97.40% of Python3 online submissions for Determine Color of a Chessboard Square.
    def squareIsWhite(self, coordinates: str) -> bool:
        return (int(coordinates[1]) - ord(coordinates[0]) - ord('0')) % 2 != 0


if __name__ == "__main__":
    so = Solution()
    print(so.squareIsWhite("h8"))