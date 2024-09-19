"""Pascal's Triangle II
https://leetcode.com/problems/pascals-triangle-ii
"""


class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        mapper = [[0] * (rowIndex + 1) for _ in range(rowIndex+1)]
        mapper[0][0] = 1
        for i in range(1, rowIndex+1):
            for j in range(i+1):
                mapper[i][j] = (
                    1 if j == 0 or mapper[i - 1][j] == 0
                    else mapper[i - 1][j - 1] + mapper[i - 1][j]
                )
        return mapper[rowIndex]


def test(rowIndex: int):
    print(Solution().getRow(rowIndex))


test(3)
test(0)
test(1)
