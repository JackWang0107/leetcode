from typing import *
class Solution:
    # 172 ms, faster than 97.80% of Python3 online submissions for Number Of Rectangles That Can Form The Largest Square.
    # 14.8 MB, less than 88.30% of Python3 online submissions for Number Of Rectangles That Can Form The Largest Square.
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        from collections import Counter
        largest_squares  = dict(Counter([min(rec) for rec in rectangles]))
        return largest_squares[max(largest_squares.keys())]
    
    # 176 ms, faster than 94.47% of Python3 online submissions for Number Of Rectangles That Can Form The Largest Square.
    # 14.7 MB, less than 96.81% of Python3 online submissions for Number Of Rectangles That Can Form The Largest Square.
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        squares = {}
        maxLen = 0
        for rec in rectangles:
            temp  = min(rec)
            if maxLen < temp:
                maxLen = temp
            try:
                squares[min(rec)] += 1
            except KeyError:
                squares[min(rec)] = 0
                squares[min(rec)] += 1
        return squares[maxLen]


if __name__ == "__main__":
    so = Solution()
    print(so.countGoodRectangles(rectangles = [[2,3],[3,7],[4,3],[3,7]]))
        