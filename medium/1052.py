"""Grumpy Bookstore Owner
https://leetcode.com/problems/grumpy-bookstore-owner
"""


class Solution:
    def maxSatisfied(
        self, customers: list[int], grumpy: list[int], minutes: int
    ) -> int:
        max_satisfied = 0
        for index, value in enumerate(grumpy):
            if value == 0:
                max_satisfied += customers[index]
        add_on = 0
        for i in range(minutes):
            if grumpy[i] == 1:
                add_on += customers[i]
        max_satisfied_overall = max_satisfied + add_on
        for i in range(minutes, len(grumpy)):
            if grumpy[i - minutes] == 1:
                add_on -= customers[i - minutes]
            if grumpy[i] == 1:
                add_on += customers[i]
            max_satisfied_overall = max(
                max_satisfied_overall, max_satisfied+add_on)
        return max_satisfied_overall


def test(customers: list[int], grumpy: list[int], minutes: int):
    print(Solution().maxSatisfied(customers, grumpy, minutes))


test([1, 0, 1, 2, 1, 1, 7, 5], [0, 1, 0, 1, 0, 1, 0, 1], 3)
test([1], [0], 1)
