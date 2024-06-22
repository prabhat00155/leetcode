"""Cheapest Flights Within K Stops
https://leetcode.com/problems/cheapest-flights-within-k-stops
"""


import heapq


class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int,
                          dst: int, k: int) -> int:
        edges = [[] for _ in range(n)]
        q = []
        prices = {(src, 0): 0}

        for u, v, price in flights:
            edges[u].append((v, price))
        heapq.heappush(q, (0, src, 0))

        while q:
            price1, u, stops = heapq.heappop(q)
            if stops <= k:
                for v, price2 in edges[u]:
                    if (
                        (v, stops + 1) not in prices
                        or price1 + price2 < prices[(v, stops + 1)]
                    ):
                        prices[(v, stops + 1)] = price1 + price2
                        heapq.heappush(q, (prices[(v, stops + 1)], v, stops+1))

        result = float('inf')

        for (node, stops), price in prices.items():
            if node == dst:
                result = min(result, price)
        return result if result != float('inf') else -1


def test(n, flights, src, dst, k):
    print(Solution().findCheapestPrice(n, flights, src, dst, k))


test(4, [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]],
     0, 3, 1)
test(3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1)
test(3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 0)
