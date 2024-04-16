"""Number of Islands
https://leetcode.com/problems/number-of-islands/
"""


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0
        m = len(grid)
        n = len(grid[0])
        visited = set()
        no_of_islands = 0

        def traverse(i, j):
            if (
                (i, j) in visited or i < 0
                or i >= m or j < 0 or j >= n or grid[i][j] == '0'
            ):
                return
            visited.add((i, j))
            traverse(i+1, j)
            traverse(i, j+1)
            traverse(i-1, j)
            traverse(i, j-1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and (i, j) not in visited:
                    traverse(i, j)
                    no_of_islands += 1

        return no_of_islands


def test(grid):
    print(Solution().numIslands(grid))


test([["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"],
      ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]])
test([["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"],
      ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]])
test([[]])
