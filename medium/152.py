"""Maximum Product Subarray
https://leetcode.com/problems/maximum-product-subarray
"""


class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        max_prod, min_prod, global_max = nums[0], nums[0], nums[0]
        for val in nums[1:]:
            if val < 0:
                max_prod, min_prod = min_prod, max_prod
            max_prod = max(val, max_prod*val)
            min_prod = min(val, min_prod*val)
            global_max = max(global_max, max_prod)
        return global_max


def test(nums):
    print(Solution().maxProduct(nums))


test([2, 3, -2, 4])
test([-2, 0, -1])
