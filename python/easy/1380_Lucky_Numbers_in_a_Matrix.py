from typing import *
class Solution:
	# 116 ms, faster than 96.82% of Python3 online submissions for Lucky Numbers in a Matrix.
	# 14.4 MB, less than 87.29% of Python3 online submissions for Lucky Numbers in a Matrix.
	def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
		ans = []
		for row in range(len(matrix)):
			row_min = min(matrix[row])
			row_min_dix = matrix[row].index(row_min)
			if_is_column_max = True
			for i in range(len(matrix)):
				if matrix[i][row_min_dix] > row_min:
					if_is_column_max = False
					break
			if if_is_column_max:
				ans.append(row_min)
		return ans


if __name__ == "__main__":
	so = Solution()
	print(so.luckyNumbers(matrix = [[7,8],[1,2]]))