from typing import *
# Time Limit Exceeded
# 61 / 68 test cases passed.
class RecentCounter:
    def __init__(self):
        self.time = []
        self.requets=0
    def ping(self, t: int) -> int:
        self.time.append(t)
        self.requets+=1
        return len(self.time) - sum(map(lambda x:t-x>3000,self.time)) # bottleneck

# 3816 ms, faster than 9.87% of Python3 online submissions for Number of Recent Calls.
# 19 MB, less than 66.25% of Python3 online submissions for Number of Recent Calls.
class RecentCounter:
    def __init__(self):
        self.time = []
        self.requets=0
    def ping(self, t: int) -> int:
        self.time.append(t)
        self.requets += 1
        idx_to_pop = []
        # dynamic maintaining self.time
        for idx, time in enumerate(self.time):
            if t - time > 3000:
                idx_to_pop.append(idx)
                self.requets -= 1
        for idx in idx_to_pop[::-1]:
            self.time.pop(idx)
        return self.requets

if __name__ == "__main__":
    rc = RecentCounter()
    print(rc.ping(642))
    print(rc.ping(1849))
    print(rc.ping(4921))
    print(rc.ping(6936))
    print(rc.ping(5957))