"""Count Distinct Numbers on Board
https://leetcode.com/problems/count-distinct-numbers-on-board
"""


class Solution:
    def distinctIntegers(self, n: int) -> int:
        turn, flag, max_days = 1, True, 10 ** 9
        board = {n}
        while flag and turn < max_days:
            flag = False
            turn += 1
            for e in list(board):
                for i in range(2, e):
                    if e % i == 1 and i not in board:
                        board.add(i)
                        flag = True
        return len(board)


def test(n):
    print(Solution().distinctIntegers(n))


test(5)
test(3)
