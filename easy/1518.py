"""Water Bottles
https://leetcode.com/problems/water-bottles
"""


class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        num = numBottles
        while numBottles >= numExchange:
            num += numBottles // numExchange
            numBottles = numBottles // numExchange + numBottles % numExchange
        return num


def test(num_bottles: int, num_exchange: int):
    print(Solution().numWaterBottles(num_bottles, num_exchange))


test(9, 3)
test(15, 4)
