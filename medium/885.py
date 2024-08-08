"""Spiral Matrix III
https://leetcode.com/problems/spiral-matrix-iii
"""


class Solution:
    def spiralMatrixIII(
        self, rows: int, cols: int, rStart: int, cStart: int
    ) -> list[list[int]]:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        result = []
        total_cells = rows * cols
        x, y = rStart, cStart
        step = 1
        direction_index = 0
        while len(result) < total_cells:
            for _ in range(2):
                dx, dy = directions[direction_index]
                for _ in range(step):
                    if 0 <= x < rows and 0 <= y < cols:
                        result.append([x, y])
                    x += dx
                    y += dy
                    if len(result) >= total_cells:
                        return result
                direction_index = (direction_index + 1) % 4
            step += 1

        return result


def test(rows, cols, rstart, cstart):
    print(Solution().spiralMatrixIII(rows, cols, rstart, cstart))


test(1, 4, 0, 0)
test(5, 6, 1, 4)
