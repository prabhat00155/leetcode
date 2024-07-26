"""Airplane Seat Assignment Probability
https://leetcode.com/problems/airplane-seat-assignment-probability
"""


class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        return 1 if n == 1 else 0.5


def test(n):
    print(Solution().nthPersonGetsNthSeat(n))


test(1)
test(2)
