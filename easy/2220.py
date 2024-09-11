"""Minimum Bit Flips to Convert Number
https://leetcode.com/problems/minimum-bit-flips-to-convert-number
"""


class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        def count_set_bits(num):
            count = 0
            while num > 0:
                count += (num & 1)
                num = num >> 1
            return count

        return count_set_bits(start ^ goal)


def test(start: int, goal: int):
    print(Solution().minBitFlips(start, goal))


test(10, 7)
test(3, 4)
