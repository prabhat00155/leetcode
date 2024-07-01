"""Find the Town Judge
https://leetcode.com/problems/find-the-town-judge
"""


class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        indegree = {}
        outdegree = {}
        for u, v in trust:
            indegree[v] = indegree.get(v, 0) + 1
            outdegree[u] = outdegree.get(u, 0) + 1
        for node in range(1, n+1):
            if indegree.get(node, 0) == n - 1 and outdegree.get(node, 0) == 0:
                return node
        return -1


def test(n, trust):
    print(Solution().findJudge(n, trust))


test(2, [[1, 2]])
test(3, [[1, 3], [2, 3]])
test(3, [[1, 3], [2, 3], [3, 1]])
