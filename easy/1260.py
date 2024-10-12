"""Shift 2D Grid
https://leetcode.com/problems/shift-2d-grid
"""


class Solution:
    def shiftGrid(self, grid: list[list[int]], k: int) -> list[list[int]]:
        rows, cols = len(grid), len(grid[0])
        output = [[None] * cols for _ in grid]

        for r in range(rows):
            for c in range(cols):
                out_r = ((r * cols + c + k) // cols) % rows
                out_c = (c + k) % cols
                output[out_r][out_c] = grid[r][c]
        return output


def test(grid: list[list[int]], k: int):
    print(Solution().shiftGrid(grid, k))


test([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1)
test([[3, 8, 1, 9], [19, 7, 2, 5], [4, 6, 11, 10], [12, 0, 21, 13]], 4)
test([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 9)
test([[1], [2], [3], [4], [7], [6], [5]], 23)
