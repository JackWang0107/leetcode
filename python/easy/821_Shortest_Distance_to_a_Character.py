from typing import *
class Solution:
	# 92 ms, faster than 18.27% of Python3 online submissions for Shortest Distance to a Character.
	# 14.5 MB, less than 27.63% of Python3 online submissions for Shortest Distance to a Character.
	def shortestToChar(self, s: str, c: str) -> List[int]:
		ids = [i for i in range(len(s)) if s[i] == c]
		return [min([abs(i-id_) for id_ in ids]) for i in range(len(s))]


if __name__ == "__main__":
	so = Solution()
	print(so.shortestToChar(s = "loveleetcode", c = "e"))