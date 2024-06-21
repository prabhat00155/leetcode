"""Cracking the Safe
https://leetcode.com/problems/cracking-the-safe
"""


class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        seen = set()
        result = []

        def dfs(u):
            for x in range(k):
                v = u + str(x)
                if v not in seen:
                    seen.add(v)
                    dfs(v[1:])
                    result.append(str(x))

        start_node = '0' * (n - 1)
        dfs(start_node)
        return ''.join(result) + start_node


def test(n, k):
    print(Solution().crackSafe(n, k))


test(2, 2)
test(1, 2)
