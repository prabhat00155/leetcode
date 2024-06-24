"""Count Ways to Build Rooms in an Ant Colony
https://leetcode.com/problems/count-ways-to-build-rooms-in-an-ant-colony
"""


import math


MOD = 10**9 + 7


class Solution:
    def waysToBuildRooms(self, prevRoom: list[int]) -> int:
        n = len(prevRoom)
        edges = [[] for _ in range(n)]
        for i in range(1, n):
            edges[prevRoom[i]].append(i)

        memo = {}

        def dfs(node):
            if node in memo:
                return memo[node]

            total_ways = 1
            total_size = 0
            for child in edges[node]:
                child_ways, child_size = dfs(child)
                total_ways = total_ways * child_ways % MOD
                total_ways = total_ways * math.comb(
                        total_size + child_size, child_size) % MOD
                total_size += child_size

            memo[node] = (total_ways, total_size + 1)
            return memo[node]

        result, _ = dfs(0)
        return result % MOD


def test(prev_room):
    print(Solution().waysToBuildRooms(prev_room))


test([-1, 0, 1])
test([-1, 0, 0, 1, 2])
