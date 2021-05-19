from typing import *
class Solution:
    # 228 ms, faster than 96.51% of Python3 online submissions for Count Items Matching a Rule.
    # 20.4 MB, less than 87.05% of Python3 online submissions for Count Items Matching a Rule.
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        idx_table = {
            "type" : 0,
            "color" : 1,
            "name" : 2
        }
        ans = 0
        idx = idx_table[ruleKey]
        for item in items:
            if item[idx] == ruleValue:
                ans +=1
        return ans


if __name__ == "__main__":
    so = Solution()
    print(
        so.countMatches(items = [["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]], ruleKey = "type", ruleValue = "phone")
    )