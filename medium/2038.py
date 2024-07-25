"""Remove Colored Pieces if Both Neighbors are the Same Color
https://leetcode.com/problems/remove-colored-pieces-if-both-neighbors-are-the-same-color
"""


class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        moves = 0
        for i in range(1, len(colors)-1):
            if colors[i] == colors[i - 1] and colors[i] == colors[i + 1]:
                moves = moves + 1 if colors[i] == 'A' else moves - 1
        return moves > 0


def test(colours):
    print(Solution().winnerOfGame(colours))


test('AAABABB')
test('AA')
test('ABBBBBBBAAA')
