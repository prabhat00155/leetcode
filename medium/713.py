"""Subarray Product Less Than K
https://leetcode.com/problems/subarray-product-less-than-k
"""


class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        i, prod, count = 0, 1, 0
        for j in range(len(nums)):
            prod *= nums[j]
            while i <= j and prod >= k:
                prod //= nums[i]
                i += 1
            count += j - i + 1
        return count


def test(nums: list[int], k: int):
    print(Solution().numSubarrayProductLessThanK(nums, k))


test([10, 5, 2, 6], 100)
test([1, 2, 3], 0)
