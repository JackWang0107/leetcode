from typing import *
class Solution:
    # 36 ms, faster than 69.51% of Python3 online submissions for Number of Students Doing Homework at a Given Time.
    # 14.1 MB, less than 80.68% of Python3 online submissions for Number of Students Doing Homework at a Given Time.
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        num = 0
        for start, end in zip(startTime, endTime):
            if start <= queryTime <= end:
                num +=1
        return num

    # 36 ms, faster than 69.51% of Python3 online submissions for Number of Students Doing Homework at a Given Time.
    # 14.2 MB, less than 80.68% of Python3 online submissions for Number of Students Doing Homework at a Given Time.
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        num = 0
        for start, end in zip(startTime, endTime):
            num += start <= queryTime <= end
        return num

    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        return sum(start <= queryTime <= end for start, end in zip(startTime, endTime))

if __name__ == "__main__":
    so = Solution()
    print(so.busyStudent(startTime = [9,8,7,6,5,4,3,2,1], endTime = [10,10,10,10,10,10,10,10,10], queryTime = 5))
