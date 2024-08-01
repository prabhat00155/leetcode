"""Minimum Operations to Make Array Equal
https://leetcode.com/problems/minimum-operations-to-make-array-equal
"""


class Solution:
    def minOperations(self, n: int) -> int:
        mid = 2 * (n // 2) + 1
        if n % 2 == 0:
            mid = (mid + 2 * (n // 2 - 1) + 1) // 2
        return sum(list(map(lambda i: mid - (2 * i + 1), range(n//2))))


def test(n):
    print(Solution().minOperations(n))


test(2)
test(3)
test(6)
test(1)
