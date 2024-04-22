"""Number of Closed Islands
https://leetcode.com/problems/number-of-closed-islands
"""


class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        visited = {}

        def traverse(i, j):
            if (i, j) in visited:
                return visited[(i, j)]

            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                return False

            visited[(i, j)] = True

            if grid[i][j] == 0:
                visited[(i, j)] = (traverse(i, j-1) and traverse(i, j+1)
                                   and traverse(i-1, j) and traverse(i+1, j))
            return visited[(i, j)]

        count = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if (
                    (x, y) not in visited and traverse(x, y)
                    and grid[x][y] == 0
                ):
                    count += 1

        return count


def test(grid):
    print(Solution().closedIsland(grid))


test([
    [1, 1, 1, 1, 1, 1, 1, 0],
    [1, 0, 0, 0, 0, 1, 1, 0],
    [1, 0, 1, 0, 1, 1, 1, 0],
    [1, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 0]
])
test([[0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 1, 1, 1, 0]])
test([
    [1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1]
])
test([[]])
