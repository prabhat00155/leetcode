"""Redundant Connection
https://leetcode.com/problems/redundant-connection
"""


class Solution:
    parent = {}

    def find(self, u):
        return u if self.parent[u] == u else self.find(self.parent[u])

    def union(self, u, v):
        self.parent[self.find(v)] = self.find(u)

    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        seen = set()
        for u, v in edges:
            if u not in seen:
                self.parent[u] = u
                seen.add(u)
            if v not in seen:
                self.parent[v] = v
                seen.add(v)
        for u, v in edges:
            if self.find(u) != self.find(v):
                self.union(u, v)
            else:
                return [u, v]
        return []


def test(edges):
    print(Solution().findRedundantConnection(edges))


test([[1, 2], [1, 3], [2, 3]])
test([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]])
