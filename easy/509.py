"""Fibonacci Number
https://leetcode.com/problems/fibonacci-number
"""


class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        a, b = 0, 1
        i = 1
        while i < n:
            a, b = b, a + b
            i += 1
        return b


def test(n: int):
    print(Solution().fib(n))


test(0)
test(1)
test(2)
test(3)
test(4)
