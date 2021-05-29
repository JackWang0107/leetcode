from typing import *
class Solution:
    # 52 ms, faster than 70.79% of Python3 online submissions for Destination City.
    # 14.5 MB, less than 16.35% of Python3 online submissions for Destination City.
    def destCity(self, paths: List[List[str]]) -> str:
        cities = {}
        for edge in paths:
            city_a, city_b = edge
            try:
                cities[city_a] += 1
            except KeyError:
                cities[city_a] = 1
            try:
                cities[city_b] -= 1
            except KeyError:
                cities[city_b] = -1
        for key, value in cities.items():
            if value == -1:
                return key

    # 48 ms, faster than 89.05% of Python3 online submissions for Destination City.
    # 14.2 MB, less than 73.56% of Python3 online submissions for Destination City.
    def destCity(self, paths: List[List[str]]) -> str:
        return (set(map(lambda x:x[1], paths)) -  set(map(lambda x:x[0], paths))).pop()


if __name__ == "__main__":
    so = Solution()
    print(so.destCity(paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]))