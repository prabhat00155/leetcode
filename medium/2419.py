"""Longest Subarray With Maximum Bitwise AND
https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and
"""


class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        i, j = 0, 0
        max_val, max_len = 0, 0
        while i < len(nums) and j < len(nums):
            if nums[i] == nums[j]:
                if nums[i] > max_val:
                    max_val = nums[i]
                    max_len = j - i + 1
                elif nums[i] == max_val:
                    max_len = max(max_len, j-i+1)
                j += 1
            else:
                i = j
        return max_len


def test(nums: list[int]):
    print(Solution().longestSubarray(nums))


test([1, 2, 3, 3, 2, 2])
test([1, 2, 3, 4])
