from typing import *
class Solution:
    # 28 ms, faster than 93.78% of Python3 online submissions for Find the Highest Altitude.
    # 14.1 MB, less than 90.02% of Python3 online submissions for Find the Highest Altitude.
        def largestAltitude(self, gain: List[int]) -> int:
            history_altitude = 0
            highest_altitude = 0
            for point in gain:
                history_altitude += point
                if history_altitude >= highest_altitude:
                    highest_altitude = history_altitude
            return highest_altitude
        
        # 36 ms, faster than 52.07% of Python3 online submissions for Find the Highest Altitude.
        # 14.1 MB, less than 68.62% of Python3 online submissions for Find the Highest Altitude.
        def largestAltitude(self, gain: List[int]) -> int:
            ans = [0]
            for point in gain:
                ans.append(ans[-1] + point)
            return max(ans)

if __name__ == "__main__":
    so = Solution()
    print(so.largestAltitude( gain = [-5,1,5,0,-7]))