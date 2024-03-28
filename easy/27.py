# Remove element
# https://leetcode.com/problems/remove-element/


class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        i = 0
        while i < len(nums):
            j = i
            while j < len(nums) and nums[j] == val:
                j += 1
            if j >= len(nums):
                break
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
        return i


def test(nums, val):
    length = Solution().removeElement(nums, val)
    print(nums[:length])


test([3, 2, 2, 3], 3)
test([0, 1, 2, 2, 3, 0, 4, 2], 2)
