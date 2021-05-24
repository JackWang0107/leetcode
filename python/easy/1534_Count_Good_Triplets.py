from typing import *
class Solution:
    # Simple but not elegant solution
    # 672 ms, faster than 60.83% of Python3 online submissions for Count Good Triplets.
    # 14 MB, less than 94.27% of Python3 online submissions for Count Good Triplets.
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        total_num = 0
        for i in range( len(arr) ):
            for j in range(i+1, len(arr)):
                for k in range(j+1, len(arr)):
                    if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                        total_num += 1
        return total_num

if __name__ == "__main__":
    so = Solution()
    print(so.countGoodTriplets( arr = [1,1,2,2,3], a = 0, b = 0, c = 1))
