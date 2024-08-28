"""Count Sub Islands
https://leetcode.com/problems/count-sub-islands
"""


class Solution:
    def countSubIslands(
        self, grid1: list[list[int]], grid2: list[list[int]]
    ) -> int:
        visited = set()

        def is_subisland(r, c):
            if (
                r < 0 or r >= len(grid2) or c < 0 or c >= len(grid2[0])
                or (r, c) in visited or grid2[r][c] == 0
            ):
                return -1
            visited.add((r, c))
            ret = int(grid1[r][c] == 1)
            ret1 = is_subisland(r+1, c)
            ret2 = is_subisland(r-1, c)
            ret3 = is_subisland(r, c+1)
            ret4 = is_subisland(r, c-1)
            return 0 if 0 in [ret, ret1, ret2, ret3, ret4] else 1

        total = 0
        for r in range(len(grid2)):
            for c in range(len(grid2[0])):
                if is_subisland(r, c) == 1:
                    total += 1
        return total


def test(grid1: list[list[int]], grid2: list[list[int]]):
    print(Solution().countSubIslands(grid1, grid2))


test([[1, 1, 1, 0, 0], [0, 1, 1, 1, 1], [0, 0, 0, 0, 0],
      [1, 0, 0, 0, 0], [1, 1, 0, 1, 1]],
     [[1, 1, 1, 0, 0], [0, 0, 1, 1, 1], [0, 1, 0, 0, 0],
      [1, 0, 1, 1, 0], [0, 1, 0, 1, 0]])
test([[1, 0, 1, 0, 1], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0],
      [1, 1, 1, 1, 1], [1, 0, 1, 0, 1]],
     [[0, 0, 0, 0, 0], [1, 1, 1, 1, 1], [0, 1, 0, 1, 0],
      [0, 1, 0, 1, 0], [1, 0, 0, 0, 1]])
