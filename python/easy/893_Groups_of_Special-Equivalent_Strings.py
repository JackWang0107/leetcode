from typing import *
class Solution:
	# 40 ms, faster than 90.81% of Python3 online submissions for Groups of Special-Equivalent Strings.
	# 14.7 MB, less than 18.83% of Python3 online submissions for Groups of Special-Equivalent Strings.
	def numSpecialEquivGroups(self, words: List[str]) -> int:
		from collections import defaultdict
		helper = defaultdict(int)
		for string in words:
			key = "".join(sorted(string[0::2])+sorted(string[1::2]))
			helper[key] += 1
		return len(helper)


if __name__ == "__main__":
	so = Solution()
	print(so.numSpecialEquivGroups(words = ["abc","acb","bac","bca","cab","cba"]))