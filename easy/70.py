"""Climbing Stairs
https://leetcode.com/problems/climbing-stairs
"""


class Solution:
    mapper = {}

    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 1
        if n < 0:
            return 0
        if n in self.mapper.keys():
            return self.mapper[n]
        self.mapper[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return self.mapper[n]


def test(n):
    print(Solution().climbStairs(n))


test(2)
test(3)
