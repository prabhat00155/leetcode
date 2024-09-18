"""Largest Number
https://leetcode.com/problems/largest-number
"""


from functools import cmp_to_key


class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        def compare(a, b):
            if a + b < b + a:
                return 1
            if a + b > b + a:
                return -1
            return 0

        arr = sorted(map(lambda x: str(x), nums), reverse=True)
        return ''.join(
            sorted(arr, key=cmp_to_key(compare))) if arr[0] != '0' else '0'


def test(nums: list[int]):
    print(Solution().largestNumber(nums))


test([10, 2])
test([3, 30, 34, 5, 9])
test([0, 0])
