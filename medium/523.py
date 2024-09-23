"""Continuous Subarray Sum
https://leetcode.com/problems/continuous-subarray-sum
"""


class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        mods = {0: -1}
        running_sum = 0
        for ind, val in enumerate(nums):
            running_sum += val
            running_sum %= k
            if running_sum in mods:
                if ind - mods[running_sum] > 1:
                    return True
            else:
                mods[running_sum] = ind
        return False


def test(nums: list[int], k: int):
    print(Solution().checkSubarraySum(nums, k))


test([23, 2, 4, 6, 7], 6)
test([23, 2, 6, 4, 7], 6)
test([23, 2, 6, 4, 7], 13)
