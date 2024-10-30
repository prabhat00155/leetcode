"""Contains Duplicate
https://leetcode.com/problems/contains-duplicate
"""


class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return len(nums) != len(set(nums))


def test(nums: list[int]) -> bool:
    return Solution().containsDuplicate(nums)


assert test([1, 2, 3, 1])
assert not test([1, 2, 3, 4])
assert test([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])
