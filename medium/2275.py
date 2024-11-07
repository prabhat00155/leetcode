"""Largest Combination With Bitwise AND Greater Than Zero

https://leetcode.com/problems/largest-combination-with-bitwise-and-greater-than-zero
"""


class Solution:
    def largestCombination(self, candidates: list[int]) -> int:
        maxima = 0
        for bit in range(32):
            count = sum((num >> bit) & 1 for num in candidates)
            maxima = max(maxima, count)
        return maxima


def test(candidates: list[int]) -> int:
    return Solution().largestCombination(candidates)


assert test([16, 17, 71, 62, 12, 24, 14]) == 4
assert test([8, 8]) == 2
