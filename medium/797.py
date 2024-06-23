"""All Paths from Source to Target
https://leetcode.com/problems/all-paths-from-source-to-target
"""


class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        all_paths = []
        n = len(graph)

        def dfs(u, cur):
            if u == n - 1:
                all_paths.append(cur)
                return
            for v in graph[u]:
                dfs(v, cur+[v])

        dfs(0, [0])
        return all_paths


def test(graph):
    print(Solution().allPathsSourceTarget(graph))


test([[1, 2], [3], [3], []])
test([[4, 3, 1], [3, 2, 4], [3], [4], []])
