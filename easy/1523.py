"""Count Odd Numbers in an Interval Range
https://leetcode.com/problems/count-odd-numbers-in-an-interval-range
"""


class Solution:
    def countOdds(self, low: int, high: int) -> int:
        count = (high - low + 1) // 2
        return count + 1 if low % 2 == 1 and high % 2 == 1 else count


def test(low: int, high: int):
    print(Solution().countOdds(low, high))


test(3, 7)
test(8, 10)
