"""Rotting Oranges
https://leetcode.com/problems/rotting-oranges
"""
from collections import deque


class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        def check(x, y, visited):
            return (0 <= x < len(grid) and 0 <= y < len(grid[0])
                    and (x, y) not in visited and grid[x][y] == 1)

        q = deque()
        visited = set()
        for xi in range(len(grid)):
            for yj in range(len(grid[0])):
                if grid[xi][yj] == 2:
                    q.append((xi, yj, 0))
                    visited.add((xi, yj))
        max_level = 0
        while q:
            i, j, level = q.popleft()
            grid[i][j] = 2
            max_level = max(max_level, level)
            if check(i-1, j, visited):
                q.append((i-1, j, level+1))
                visited.add((i-1, j))
            if check(i+1, j, visited):
                q.append((i+1, j, level+1))
                visited.add((i+1, j))
            if check(i, j-1, visited):
                q.append((i, j-1, level+1))
                visited.add((i, j-1))
            if check(i, j+1, visited):
                q.append((i, j+1, level+1))
                visited.add((i, j+1))
        for xi in range(len(grid)):
            for yj in range(len(grid[0])):
                if grid[xi][yj] == 1:
                    return -1
        return max_level


def test(grid):
    print(Solution().orangesRotting(grid))


test([[2, 1, 1], [1, 1, 0], [0, 1, 1]])
test([[2, 1, 1], [0, 1, 1], [1, 0, 1]])
test([[0, 2]])
test([[]])
