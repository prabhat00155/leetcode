"""Find Minimum in Rotated Sorted Array II
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii
"""


class Solution:
    def findMin(self, nums: list[int]) -> int:
        first, last = 0, len(nums) - 1
        if nums[first] == nums[last]:
            return min(nums)
        while first <= last:
            if nums[first] < nums[last]:
                return nums[first]
            middle = first + (last - first) // 2
            if nums[middle] <= nums[last]:
                if middle > 0 and nums[middle - 1] > nums[middle]:
                    return nums[middle]
                if (
                    middle < len(nums) - 1
                    and nums[middle + 1] < nums[middle - 1]
                    and nums[last] < nums[first]
                ):
                    first = middle + 1
                else:
                    last = middle - 1
            else:
                if (
                    middle > 0
                    and nums[middle - 1] < nums[middle + 1]
                    and nums[first] < nums[last]
                ):
                    last = middle - 1
                else:
                    first = middle + 1
        return nums[first]


def test(nums):
    print(Solution().findMin(nums))


test([1, 3, 5])
test([2, 2, 2, 0, 1])
