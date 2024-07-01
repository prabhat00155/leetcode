"""Maximal Network Rank
https://leetcode.com/problems/maximal-network-rank
"""


class Solution:
    def maximalNetworkRank(self, n: int, roads: list[list[int]]) -> int:
        edges = [[0] * n for _ in range(n)]
        degree = [0] * n
        maxima = -float('inf')

        for u, v in roads:
            edges[u][v] = 1
            edges[v][u] = 1
            degree[u] += 1
            degree[v] += 1

        for i in range(n-1):
            for j in range(i+1, n):
                rank = (degree[i] + degree[j]
                        if edges[i][j] == 0 else degree[i] + degree[j] - 1)
                maxima = max(maxima, rank)

        return maxima


def test(n, roads):
    print(Solution().maximalNetworkRank(n, roads))


test(4, [[0, 1], [0, 3], [1, 2], [1, 3]])
test(5, [[0, 1], [0, 3], [1, 2], [1, 3], [2, 3], [2, 4]])
test(8, [[0, 1], [1, 2], [2, 3], [2, 4], [5, 6], [5, 7]])
