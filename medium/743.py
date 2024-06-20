"""Network Delay Time
https://leetcode.com/problems/network-delay-time
"""


import heapq


class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        edges = [[] for _ in range(n)]
        cost = [float('inf')] * n
        q = []

        for item in times:
            edges[item[0] - 1].append((item[1] - 1, item[2]))
        heapq.heappush(q, (0, k-1))
        cost[k - 1] = 0

        while q:
            c1, u = heapq.heappop(q)
            if c1 <= cost[u]:
                for v, c2 in edges[u]:
                    if c1 + c2 < cost[v]:
                        cost[v] = c1 + c2
                        heapq.heappush(q, (cost[v], v))

        return -1 if float('inf') in cost else max(cost)


def test(times, n, k):
    print(Solution().networkDelayTime(times, n, k))


test([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2)
test([[1, 2, 1]], 2, 1)
test([[1, 2, 1]], 2, 2)
