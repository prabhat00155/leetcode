"""Number of Provinces
https://leetcode.com/problems/number-of-provinces
"""


class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        visited = set()
        count = 0

        def dfs(node):
            for n, v in enumerate(isConnected[node]):
                if n != node and v == 1 and n not in visited:
                    visited.add(n)
                    dfs(n)

        for n in range(len(isConnected)):
            if n not in visited:
                dfs(n)
                count += 1
        return count


def test(is_connected):
    print(Solution().findCircleNum(is_connected))


test([[1, 1, 0], [1, 1, 0], [0, 0, 1]])
test([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
