"""Maximum Subarray

https://leetcode.com/problems/maximum-subarray
"""


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        cur, maxima = 0, -float('inf')
        for val in nums:
            cur = cur + val if cur + val > val else val
            maxima = max(maxima, cur)
        return maxima


def test(nums: list[int]) -> int:
    return Solution().maxSubArray(nums)


assert test([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
assert test([1]) == 1
assert test([5, 4, -1, 7, 8]) == 23
