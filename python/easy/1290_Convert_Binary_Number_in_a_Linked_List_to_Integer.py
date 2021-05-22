from typing import *
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def getDecimalValue(self, head) -> int:
        ans = 0
        while head:
            ans = ans*10 + head.val
            head = head.next
        return int(str(ans), 2)

if __name__ == "__main__":
    so = Solution()
    print(so.getDecimalValue( head = [1,0,1]))