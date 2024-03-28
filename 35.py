"""Search Insert Position
https://leetcode.com/problems/search-insert-position/
"""


class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        if not nums:
            return 0
        first = 0
        last = len(nums) - 1
        middle = first + (last - first) // 2
        while first <= last:
            middle = first + (last - first) // 2
            if target == nums[middle]:
                return middle
            if target < nums[middle]:
                last = middle - 1
            else:
                first = middle + 1
        if target < nums[middle]:
            return middle
        return middle + 1


def test(nums, target):
    print(Solution().searchInsert(nums, target))


test([1, 3, 5, 6], 5)
test([1, 3, 5, 6], 2)
test([1, 3, 5, 6], 7)
test([], 7)
test(None, 7)
