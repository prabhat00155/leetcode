"""Count Pairs of Points With Distance k
https://leetcode.com/problems/count-pairs-of-points-with-distance-k
"""


class Solution:
    def countPairs(self, coordinates: list[list[int]], k: int) -> int:
        count = 0
        seen = {}

        for x, y in coordinates:
            for operand in range(k+1):
                x2 = x ^ operand
                y2 = y ^ (k - operand)
                if (x2, y2) in seen:
                    count += seen[(x2, y2)]
            seen[(x, y)] = seen.get((x, y), 0) + 1
        return count


def test(coordinates, k):
    print(Solution().countPairs(coordinates, k))


test([[1, 2], [4, 2], [1, 3], [5, 2]], 5)
test([[1, 3], [1, 3], [1, 3], [1, 3], [1, 3]], 0)
