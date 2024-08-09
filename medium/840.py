"""Magic Squares In Grid
https://leetcode.com/problems/magic-squares-in-grid
"""


class Solution:
    def numMagicSquaresInside(self, grid: list[list[int]]) -> int:
        def is_magic_square(i, j):
            seen = set()
            for r in range(i, i+3):
                for c in range(j, j+3):
                    if 1 <= grid[r][c] <= 9 and grid[r][c] not in seen:
                        seen.add(grid[r][c])
                    else:
                        return False
            if (
                grid[i][j] + grid[i][j+1] + grid[i][j+2]
                == grid[i+1][j] + grid[i+1][j+1] + grid[i+1][j+2]
                == grid[i+2][j] + grid[i+2][j+1] + grid[i+2][j+2]
                == grid[i][j] + grid[i+1][j] + grid[i+2][j]
                == grid[i][j+1] + grid[i+1][j+1] + grid[i+2][j+1]
                == grid[i][j+2] + grid[i+1][j+2] + grid[i+2][j+2]
                == grid[i][j] + grid[i+1][j+1] + grid[i+2][j+2]
                == grid[i+2][j] + grid[i+1][j+1] + grid[i][j+2]
            ):
                return True
            return False

        if len(grid) < 3 or len(grid[0]) < 3:
            return 0
        count = 0
        for r in range(len(grid)-2):
            for c in range(len(grid[0])-2):
                if is_magic_square(r, c):
                    count += 1
        return count


def test(grid: list[list[int]]):
    print(Solution().numMagicSquaresInside(grid))


test([[4, 3, 8, 4], [9, 5, 1, 9], [2, 7, 6, 2]])
test([[8]])
