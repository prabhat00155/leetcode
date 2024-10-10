"""Complement of Base 10 Integer
https://leetcode.com/problems/complement-of-base-10-integer
"""


import math


class Solution:
    def bitwiseComplement(self, n: int) -> int:
        return 1 if n == 0 else n ^ (2 ** (int(math.log2(n)) + 1) - 1)


def test(n: int):
    print(Solution().bitwiseComplement(n))


test(5)
test(7)
test(10)
test(0)
