"""Cells with Odd Values in a Matrix
https://leetcode.com/problems/cells-with-odd-values-in-a-matrix
"""


class Solution:
    def oddCells(self, m: int, n: int, indices: list[list[int]]) -> int:
        mat = [[0] * n for _ in range(m)]
        for index in indices:
            r, c = index[0], index[1]
            for j in range(n):
                mat[r][j] += 1
            for i in range(m):
                mat[i][c] += 1
        count = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] % 2 != 0:
                    count += 1
        return count


def test(m, n, indices):
    print(Solution().oddCells(m, n, indices))


test(2, 3, [[0, 1], [1, 1]])
test(2, 2, [[1, 1], [0, 0]])
