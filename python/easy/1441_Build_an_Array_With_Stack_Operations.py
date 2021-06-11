from typing import *
class Solution:
	# 44 ms, faster than 10.49% of Python3 online submissions for Build an Array With Stack Operations.
	# 14.2 MB, less than 75.33% of Python3 online submissions for Build an Array With Stack Operations.
	def buildArray(self, target: List[int], n: int) -> List[str]:
		ans = []
		target.insert(0,0)
		for i in range(1, len(target)):
			ans.extend(["Push", "Pop"]*(target[i] - target[i-1] -1))
			ans.append("Push")
		return ans


if __name__ == "__main__":
	so = Solution()
	print(so.buildArray(target = [2,3,4], n = 4))