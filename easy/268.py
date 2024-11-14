"""Missing Number

https://leetcode.com/problems/missing-number
"""


class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        return int(len(nums) * (len(nums) + 1) / 2) - sum(nums)


def test(nums: list[int]) -> int:
    return Solution().missingNumber(nums)


assert test([3, 0, 1]) == 2
assert test([0, 1]) == 2
assert test([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8
