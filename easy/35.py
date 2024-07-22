"""Search Insert Position
https://leetcode.com/problems/search-insert-position/
"""


class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        while start <= end:
            middle = start + (end - start) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                end = middle - 1
            else:
                start = middle + 1
        return start


def test(nums, target):
    print(Solution().searchInsert(nums, target))


test([1, 3, 5, 6], 5)
test([1, 3, 5, 6], 2)
test([1, 3, 5, 6], 7)
test([], 7)
