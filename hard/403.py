"""Frog Jump
https://leetcode.com/problems/frog-jump
"""


class Solution:
    def canCross(self, stones: list[int]) -> bool:
        positions = set(stones)
        mapper = {}

        def cross(k, value):
            if (k, value) in mapper:
                return mapper[(k, value)]
            if value not in positions:
                return False
            if value == stones[- 1]:
                return True
            res = False
            if k - 1 > 0:
                res = res or cross(k-1, value+k-1)
            mapper[(k, value)] = res or cross(k, value+k) or cross(
                    k+1, value+k+1)
            return mapper[(k, value)]

        return cross(1, 1)


def test(stones):
    print(Solution().canCross(stones))


test([0, 1, 3, 5, 6, 8, 12, 17])
test([0, 1, 2, 3, 4, 8, 9, 11])
