"""Pow(x, n)
https://leetcode.com/problems/powx-n/
"""


class Solution:
    def power(self, x, n):
        if x == 1 or n == 0:
            return 1
        if x == 0:
            return 0
        res = self.power(x, n // 2)
        return res * res if n % 2 == 0 else x * res * res

    def myPow(self, x: float, n: int) -> float:
        return self.power(x, n) if n >= 0 else 1 / self.power(x, -n)


def test(x, n):
    print(f'{x}^{n} = {Solution().myPow(x, n)}')


test(2, 3)
test(-3, 8)
test(1, 0)
test(0, 1)
test(3, -2)
