"""Reconstruct Itinerary
https://leetcode.com/problems/reconstruct-itinerary
"""
from collections import defaultdict


class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        edges = defaultdict(list)
        output = []

        for source, dest in tickets:
            edges[source].append(dest)

        for k, v in edges.items():
            v.sort(reverse=True)

        def dfs(node):
            if node in edges:
                while edges[node]:
                    dest = edges[node].pop()
                    dfs(dest)
            output.append(node)

        dfs('JFK')
        return output[::-1]


def test(tickets):
    print(Solution().findItinerary(tickets))


test([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]])
test([["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"],
      ["ATL", "JFK"], ["ATL", "SFO"]])
