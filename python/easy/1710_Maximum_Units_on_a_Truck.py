from typing import *
class Solution:
	# 148 ms, faster than 89.81% of Python3 online submissions for Maximum Units on a Truck.
	# 14.8 MB, less than 42.92% of Python3 online submissions for Maximum Units on a Truck.
	def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
		boxTypes.sort(key=lambda x:x[1], reverse=True)
		ans = 0
		type_idx = 0
		for type in boxTypes:
			if truckSize <= type[0]:
				ans += truckSize * type[1]
				break
			else:
				ans += type[0] * type[1]
				truckSize -= type[0]
		return ans


if __name__ == "__main__":
	so = Solution()
	print(so.maximumUnits(boxTypes = [[5,10],[2,5],[4,7],[3,9]], truckSize = 10))