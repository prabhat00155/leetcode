"""Two Sum
https://leetcode.com/problems/two-sum
"""


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        location = {}

        for index, value in enumerate(nums):
            if value in location:
                return [location[value], index]
            location[target - value] = index

        return []


def test(nums, target):
    print(Solution().twoSum(nums, target))


test([2, 7, 11, 15],  9)
test([3, 2, 4],  6)
test([3, 3],  6)
