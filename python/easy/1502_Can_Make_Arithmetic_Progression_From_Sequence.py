from typing import *
class Solution:
	# 40 ms, faster than 64.57% of Python3 online submissions for Can Make Arithmetic Progression From Sequence.
	# 14.2 MB, less than 95.92% of Python3 online submissions for Can Make Arithmetic Progression From Sequence.
	def canMakeArithmeticProgression(self, arr: List[int]) -> bool: 
		arr.sort()
		temp = arr[1] - arr[0] 
		for i in range(2, len(arr)):
			if arr[i] - arr[i-1] != temp:
				return False
		return True


if __name__ == "__main__":
	so = Solution()
	print(so.canMakeArithmeticProgression(arr = [1,2,4]))