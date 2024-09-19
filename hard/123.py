"""Best Time to Buy and Sell Stock III
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii
"""


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if not prices:
            return 0

        left_profit = [0] * len(prices)
        min_price = prices[0]
        for i in range(1, len(prices)):
            min_price = min(min_price, prices[i])
            left_profit[i] = max(left_profit[i - 1], prices[i]-min_price)

        right_profit = [0] * len(prices)
        max_price = prices[-1]
        for i in reversed(range(len(prices)-1)):
            max_price = max(max_price, prices[i])
            right_profit[i] = max(right_profit[i + 1], max_price-prices[i])

        max_profit = 0
        for i in range(len(prices)):
            max_profit = max(max_profit, left_profit[i]+right_profit[i])
        return max_profit


def test(prices: list[int]):
    print(Solution().maxProfit(prices))


test([3, 3, 5, 0, 0, 3, 1, 4])
test([1, 2, 3, 4, 5])
test([7, 6, 4, 3, 1])
test([2, 1, 4])
