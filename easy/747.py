"""Largest Number At Least Twice of Others
https://leetcode.com/problems/largest-number-at-least-twice-of-others
"""


class Solution:
    def dominantIndex(self, nums: list[int]) -> int:
        if not nums or len(nums) < 2:
            return -1
        largest_1, largest_2 = 0, 1
        if nums[0] < nums[1]:
            largest_1, largest_2 = 1, 0
        index = 2
        while index < len(nums):
            if nums[index] >= nums[largest_1]:
                largest_2 = largest_1
                largest_1 = index
            elif nums[index] > nums[largest_2]:
                largest_2 = index
            index += 1
        return largest_1 if nums[largest_1] >= 2 * nums[largest_2] else -1


def test(nums):
    print(Solution().dominantIndex(nums))


test([3, 6, 1, 0])
test([1, 2, 3, 4])
