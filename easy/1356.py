"""Sort Integers by The Number of 1 Bits
https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits
"""


class Solution:
    def sortByBits(self, arr: list[int]) -> list[int]:
        def count_ones(num):
            count, n = 0, num
            while num > 0:
                count += num & 1
                num >>= 1
            return count, n

        return sorted(arr, key=count_ones)


def test(arr: list[int]):
    print(Solution().sortByBits(arr))


test([1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1])
test([0, 1, 2, 3, 4, 5, 6, 7, 8])
