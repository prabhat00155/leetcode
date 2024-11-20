"""Coin Change

https://leetcode.com/problems/coin-change
"""


class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        mapper = {}

        def calculate(amount):
            if amount == 0:
                return 0
            if amount < 0:
                return float('inf')
            if amount not in mapper:
                mapper[amount] = 1 + min([calculate(amount-x) for x in coins])
            return mapper[amount]

        minima = calculate(amount)
        return minima if minima != float('inf') else -1


def test(coins: list[int], amount: int) -> int:
    return Solution().coinChange(coins, amount)


assert test([1, 2, 5], 11) == 3
assert test([2], 3) == -1
assert test([1], 0) == 0
assert test([1, 2, 5], 100) == 20
