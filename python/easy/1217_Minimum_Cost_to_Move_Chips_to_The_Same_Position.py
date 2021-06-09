from typing import *
class Solution:
    # Wrong ans for sample [6,4,7,8,2,10,2,7,9,7]
    # I think all numbers should go to the most common position that make moves least
    # but in the above sample, go to 7 takes more move to go to 6
    def minCostToMoveChips(self, position: List[int]) -> int:
        from collections import defaultdict
        max_pos, max_pos_time = 0, 0
        post_dict = defaultdict(int)
        for i in position:
            post_dict[i] += 1
            if max_pos_time < post_dict[i]:
                max_pos_time = post_dict[i]
                max_pos = i
        print(dict(post_dict))
        ans = 0
        for key, value in post_dict.items():
            print(key, value, value* ( abs(key-max_pos)%2))
            ans += value * (abs(key-max_pos) % 2)
        return ans
        
    # 24 ms, faster than 97.16% of Python3 online submissions for Minimum Cost to Move Chips to The Same Position.
    # 14.1 MB, less than 75.24% of Python3 online submissions for Minimum Cost to Move Chips to The Same Position.
    def minCostToMoveChips(self, position: List[int]) -> int:
        even = sum(map(lambda x: x%2==0, position))
        return min(even, len(position) - even)


if __name__ == "__main__":
    so = Solution()
    print(so.minCostToMoveChips([6,4,7,8,2,10,2,7,9,7]))