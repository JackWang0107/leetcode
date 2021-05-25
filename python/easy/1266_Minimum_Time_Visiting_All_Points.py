from typing import*
class Solution:
    # Stupid but easy to understand
    # 2820 ms, faster than 5.00% of Python3 online submissions for Minimum Time Visiting All Points.
    # 14.3 MB, less than 36.97% of Python3 online submissions for Minimum Time Visiting All Points.
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        def sign(x):
            if 0 < x:
                return 1
            elif x == 0:
                return 0
            else:
                return -1
        temp_point = points[0]
        total_secs = 0
        for point in points[1:]:
            while temp_point[0] != point[0] or temp_point[1] != point[1]:
                temp_point[0] += sign(point[0] - temp_point[0])
                temp_point[1] += sign(point[1] - temp_point[1])
                total_secs += 1
        return total_secs

    # finding maximum edge 
    # 52 ms, faster than 93.91% of Python3 online submissions for Minimum Time Visiting All Points.
    # 14.1 MB, less than 87.09% of Python3 online submissions for Minimum Time Visiting All Points.
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        timer = 0
        for i in range(len(points)-1):
            dx = abs(points[i+1][0] - points[i][0])
            dy = abs(points[i+1][1] - points[i][1])
            timer = timer + max(dx,dy)
        return timer


if __name__ == "__main__":
    so = Solution()
    print(so.minTimeToVisitAllPoints( points = [[1,1],[3,4],[-1,0]]))
