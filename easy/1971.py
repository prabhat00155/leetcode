"""Find if Path exists in Graph

"""


class Solution:
    def validPath(
        self,
        n: int,
        edges: list[list[int]],
        source: int,
        destination: int
    ) -> bool:
        graph = [[] for _ in range(n)]
        traversed = set()

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node):
            if node == destination:
                return True
            for node2 in graph[node]:
                if node2 not in traversed:
                    traversed.add(node2)
                    if dfs(node2):
                        return True
            return False

        traversed.add(source)
        return dfs(source)


def test(n, edges, source, destination):
    print(Solution().validPath(n, edges, source, destination))


test(3, [[0, 1], [1, 2], [2, 0]], 0, 2)
test(6, [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], 0, 5)
