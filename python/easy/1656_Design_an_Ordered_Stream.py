from sys import path
from typing import *
# 220 ms, faster than 55.41% of Python3 online submissions for Design an Ordered Stream.
# 14.9 MB, less than 93.39% of Python3 online submissions for Design an Ordered Stream.
class OrderedStream:
    def __init__(self, n: int):
        self.stream = {}
        self.ptr = 1

    def insert(self, idKey: int, value: str) -> List[str]:
        self.stream[idKey] = value
        ans = []
        while self.ptr in self.stream.keys():
            ans.append(self.stream[self.ptr])
            self.ptr += 1
        return ans

#  220 ms, faster than 55.41% of Python3 online submissions for Design an Ordered Stream.
# 15.3 MB, less than 7.92% of Python3 online submissions for Design an Ordered Stream.
class OrderedStream:
    def __init__(self, n: int):
        self.stream = {i:i for i in range(1,n+2)}
        self.ptr = 1

    def insert(self, idKey: int, value: str) -> List[str]:
        self.stream[idKey] = value
        ans = []
        while self.stream[self.ptr] != self.ptr:
            ans.append(self.stream[self.ptr])
            self.ptr += 1
        return ans

if __name__ == "__main__":
    os = OrderedStream(5)
    print(os.insert(3, "ccccc")); # Inserts (3, "ccccc"), returns [].
    print(os.insert(1, "aaaaa")); # Inserts (1, "aaaaa"), returns ["aaaaa"].
    print(os.insert(2, "bbbbb")); # Inserts (2, "bbbbb"), returns ["bbbbb", "ccccc"].
    print(os.insert(5, "eeeee")); # Inserts (5, "eeeee"), returns [].
    print(os.insert(4, "ddddd")); # Inserts (4, "ddddd"), returns ["ddddd", "eeeee"].