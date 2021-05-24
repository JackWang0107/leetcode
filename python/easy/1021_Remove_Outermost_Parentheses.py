from typing import *
class Solution:
    # 40 ms, faster than 52.11% of Python3 online submissions for Remove Outermost Parentheses.
    # 14.3 MB, less than 62.11% of Python3 online submissions for Remove Outermost Parentheses.
    def removeOuterParentheses(self, s: str) -> str:
        split_points = []
        deepth = 0
        for i in range(len(s)):
            if deepth == 0:
                split_points.append(i)
            if s[i] == "(":
                deepth += 1
            elif s[i] == ")":
                deepth -= 1
            if deepth == 0:
                split_points.append(i)
        ans = ""
        for left_point, right_point in zip(split_points[::2], split_points[1::2]):
            ans += s[left_point+1:right_point]
        return ans

    # 32 ms, faster than 92.36% of Python3 online submissions for Remove Outermost Parentheses
    # 14.5 MB, less than 34.32% of Python3 online submissions for Remove Outermost Parentheses.
    def removeOuterParentheses(self, s: str) -> str:
        split_point = []
        deepth = 0
        ans = ""
        for i in range(len(s)):
            if deepth == 0:
                split_point.append(i)
            if s[i] == "(":
                deepth += 1
            elif s[i] == ")":
                deepth -= 1
            if deepth == 0:
                split_point.append(i)
            if len(split_point) == 2:
                ans += s[split_point[0]+1 : split_point[1]]
                split_point= []
        return ans

if __name__ == "__main__":
    so = Solution()
    print(so.removeOuterParentheses(s = "(()())(())(()(()))"))