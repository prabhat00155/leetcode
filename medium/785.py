"""Is Graph Bipartite?
https://leetcode.com/problems/is-graph-bipartite
"""


from collections import deque


class Solution:
    def isBipartite(self, graph: list[list[int]]) -> bool:
        colour = {}

        def two_colour(node):
            if node in colour:
                return True

            colour[node] = 0
            q = deque()
            q.append(node)

            while q:
                u = q.popleft()
                for v in graph[u]:
                    if v not in colour:
                        colour[v] = 1 - colour[u]
                        q.append(v)
                    elif colour[u] == colour[v]:
                        return False
            return True

        for i in range(len(graph)):
            if i not in colour:
                if not two_colour(i):
                    return False
        return True


def test(graph):
    print(Solution().isBipartite(graph))


test([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]])
test([[1, 3], [0, 2], [1, 3], [0, 2]])
