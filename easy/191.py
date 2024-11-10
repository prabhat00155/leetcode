"""Number of 1 Bits

https://leetcode.com/problems/number-of-1-bits
"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n > 0:
            if n & 1 == 1:
                count += 1
            n >>= 1
        return count


def test(n: int) -> int:
    return Solution().hammingWeight(n)


assert test(11) == 3
assert test(128) == 1
assert test(2147483645) == 30
