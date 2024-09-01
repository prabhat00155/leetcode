"""Convert 1D Array Into 2D Array
https://leetcode.com/problems/convert-1d-array-into-2d-array
"""


class Solution:
    def construct2DArray(
        self, original: list[int], m: int, n: int
    ) -> list[list[int]]:
        if m * n != len(original):
            return []
        output = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                output[i][j] = original[i * n + j]
        return output


def test(original: list[int], m: int, n: int):
    print(Solution().construct2DArray(original, m, n))


test([1, 2, 3, 4], 2, 2)
test([1, 2, 3], 1, 3)
test([1, 2], 1, 1)
