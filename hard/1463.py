"""Cherry Pickup II
https://leetcode.com/problems/cherry-pickup-ii
"""


class Solution:
    def cherryPickup(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        mapper = {}

        def traverse(r, c1, c2):
            if (
                r < 0 or r >= rows or c1 < 0
                or c1 >= cols or c2 < 0 or c2 >= cols
            ):
                return 0

            cur = grid[r][c1] if c1 == c2 else grid[r][c1] + grid[r][c2]
            if r == rows - 1:
                return cur

            if (r, c1, c2) not in mapper:
                maxima = 0
                for col1 in [c1 - 1, c1, c1 + 1]:
                    for col2 in [c2 - 1, c2, c2 + 1]:
                        maxima = max(maxima, traverse(r+1, col1, col2))
                mapper[(r, c1, c2)] = cur + maxima
            return mapper[(r, c1, c2)]

        return traverse(0, 0, cols-1)


def test(grid: list[list[int]]):
    print(Solution().cherryPickup(grid))


test([[3, 1, 1], [2, 5, 1], [1, 5, 5], [2, 1, 1]])
test([
    [1, 0, 0, 0, 0, 0, 1],
    [2, 0, 0, 0, 0, 3, 0],
    [2, 0, 9, 0, 0, 0, 0],
    [0, 3, 0, 5, 4, 0, 0],
    [1, 0, 2, 3, 0, 0, 6],
])
