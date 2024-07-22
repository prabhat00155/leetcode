"""Divide Two Integers
https://leetcode.com/problems/divide-two-integers
"""


class Solution:
    def clip(self, num):
        if num > 2 ** 31 - 1:
            return 2 ** 31 - 1
        if num < -(2 ** 31):
            return -(2 ** 31)
        return num

    def divide(self, dividend: int, divisor: int) -> int:
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
        dividend, divisor = abs(dividend), abs(divisor)
        if dividend == 0 or divisor == 1:
            return self.clip(dividend * sign)
        quotient = 0
        for i in reversed(range(32)):
            if dividend >> i >= divisor:
                dividend -= divisor << i
                quotient += 1 << i
        return self.clip(quotient * sign)


def test(dividend, divisor):
    print(Solution().divide(dividend, divisor))


test(10, 3)
test(7, -3)
