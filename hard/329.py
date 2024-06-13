"""Longest Increasing Path in a Matrix
https://leetcode.com/problems/longest-increasing-path-in-a-matrix
"""


class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        longest = [[-1] * len(matrix[0]) for _ in matrix]

        def traverse(r, c):
            if longest[r][c] != -1:
                return longest[r][c]
            right = 1
            left = 1
            up = 1
            down = 1

            if 0 <= r + 1 < len(matrix) and matrix[r][c] < matrix[r+1][c]:
                right = 1 + traverse(r+1, c)
            if 0 <= r - 1 < len(matrix) and matrix[r][c] < matrix[r-1][c]:
                left = 1 + traverse(r-1, c)
            if 0 <= c + 1 < len(matrix[0]) and matrix[r][c] < matrix[r][c+1]:
                down = 1 + traverse(r, c+1)
            if 0 <= c - 1 < len(matrix[0]) and matrix[r][c] < matrix[r][c-1]:
                up = 1 + traverse(r, c-1)
            longest[r][c] = max(right, left, down, up)
            return longest[r][c]

        maxima = 1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                maxima = max(maxima, traverse(i, j))
        return maxima


def test(matrix):
    print(Solution().longestIncreasingPath(matrix))


test([[9, 9, 4], [6, 6, 8], [2, 1, 1]])
test([[3, 4, 5], [3, 2, 6], [2, 2, 1]])
test([[1]])
