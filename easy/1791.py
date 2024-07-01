"""Find Centre of Star Graph
https://leetcode.com/problems/find-center-of-star-graph
"""


class Solution:
    def findCenter(self, edges: list[list[int]]) -> int:
        degrees = {}
        for u, v in edges:
            degrees[u] = degrees.get(u, 0) + 1
            degrees[v] = degrees.get(v, 0) + 1
        for node, degree in degrees.items():
            if degree == len(degrees) - 1:
                return node
        return -1


def test(edges):
    print(Solution().findCenter(edges))


test([[1, 2], [2, 3], [4, 2]])
test([[1, 2], [5, 1], [1, 3], [1, 4]])
