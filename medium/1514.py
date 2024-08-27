"""Path with Maximum Probability
https://leetcode.com/problems/path-with-maximum-probability
"""


import heapq


class Solution:
    def maxProbability(
        self, n: int, edges: list[list[int]], succProb: list[float],
        start_node: int, end_node: int
    ) -> float:
        graph = [[] for _ in range(n)]
        for index, edge in enumerate(edges):
            u, v = edge
            proba = succProb[index]
            graph[u].append((v, proba))
            graph[v].append((u, proba))
        max_heap = [(-1, start_node)]
        probabilities = [0] * n
        probabilities[start_node] = 1

        while max_heap:
            cur_proba, cur_node = heapq.heappop(max_heap)
            cur_proba = -cur_proba
            if cur_node == end_node:
                return cur_proba
            for node, proba in graph[cur_node]:
                new_proba = proba * cur_proba
                if new_proba > probabilities[node]:
                    probabilities[node] = new_proba
                    heapq.heappush(max_heap, (-new_proba, node))
        return 0


def test(
    n: int, edges: list[list[int]], succ_proba: list[float],
    start_node: int, end_node: int
):
    print(
        Solution().maxProbability(n, edges, succ_proba, start_node, end_node)
    )


test(3, [[0, 1], [1, 2], [0, 2]], [0.5, 0.5, 0.3], 0, 2)
test(3, [[0, 1], [1, 2], [0, 2]], [0.5, 0.5, 0.2], 0, 2)
test(3, [[0, 1]], [0.5], 0, 2)
