"""Unique Paths II
https://leetcode.com/problems/unique-paths-ii
"""


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        paths = [[-1] * n for _ in range(m)]

        def unique_paths(i, j):
            if 0 <= i < m and 0 <= j < n:
                if obstacleGrid[i][j] == 1:
                    return 0
                if i == m - 1 and j == n - 1:
                    return 1
                if paths[i][j] == -1:
                    paths[i][j] = unique_paths(i+1, j) + unique_paths(i, j+1)
                return paths[i][j]
            return 0

        return unique_paths(0, 0)


def test(grid):
    print(Solution().uniquePathsWithObstacles(grid))


test([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
test([[0, 1], [0, 0]])
