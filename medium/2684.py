"""Maximum Number of Moves in a Grid
https://leetcode.com/problems/maximum-number-of-moves-in-a-grid
"""


class Solution:
    def maxMoves(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        mapper = {}

        def moves(r, c, prev=-float('inf')):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] <= prev:
                return 0
            if (r, c) not in mapper:
                mapper[(r, c)] = 1 + max(
                    moves(r-1, c+1, grid[r][c]), moves(r, c+1, grid[r][c]),
                    moves(r+1, c+1, grid[r][c]))
            return mapper[(r, c)]

        maxima = 0
        for r in range(rows):
            maxima = max(maxima, moves(r, 0))
        return maxima - 1 if maxima else 0


def test(grid: list[list[int]]) -> int:
    return Solution().maxMoves(grid)


assert test([[2, 4, 3, 5], [5, 4, 9, 3], [3, 4, 2, 11], [10, 9, 13, 15]]) == 3
assert test([[3, 2, 4], [2, 1, 9], [1, 1, 7]]) == 0
