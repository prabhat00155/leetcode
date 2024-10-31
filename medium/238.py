"""Product of Array Except Self
https://leetcode.com/problems/product-of-array-except-self
"""


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        left, right = [1] * len(nums), [1] * len(nums)
        output = []
        for i in range(1, len(nums)):
            left[i] = left[i - 1] * nums[i - 1]
        for j in range(len(nums)-2, -1, -1):
            right[j] = right[j + 1] * nums[j + 1]
        for i in range(len(nums)):
            output.append(left[i]*right[i])
        return output


def test(nums: list[int]) -> list[int]:
    return Solution().productExceptSelf(nums)


assert test([1, 2, 3, 4]) == [24, 12, 8, 6]
assert test([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
