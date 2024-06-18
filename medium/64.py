"""Minimum Path Sum
https://leetcode.com/problems/minimum-path-sum
"""


class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        saved_results = [[-1] * n for _ in range(m)]

        def min_path(i, j):
            if i == m - 1 and j == n - 1:
                return grid[i][j]
            if 0 <= i < m and 0 <= j < n:
                if saved_results[i][j] == -1:
                    saved_results[i][j] = grid[i][j] + min(
                            min_path(i+1, j), min_path(i, j+1))
                return saved_results[i][j]
            return float('inf')

        return min_path(0, 0)


def test(grid):
    print(Solution().minPathSum(grid))


test([[1, 3, 1], [1, 5, 1], [4, 2, 1]])
test([[1, 2, 3], [4, 5, 6]])
