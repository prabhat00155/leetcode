"""Maximum Sum of Distinct Subarrays With Length K

https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k
"""


class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        freq = {}
        duplicates = set()
        max_sum, cur = 0, 0
        i, j = 0, 0
        while j < len(nums):
            if j >= k:
                if len(duplicates) == 0:
                    max_sum = max(max_sum, cur)
                cur -= nums[i]
                freq[nums[i]] -= 1
                if freq[nums[i]] == 1:
                    duplicates.remove(nums[i])
                i += 1
            cur += nums[j]
            freq[nums[j]] = freq.get(nums[j], 0) + 1
            if freq[nums[j]] > 1:
                duplicates.add(nums[j])
            j += 1
        if len(duplicates) == 0:
            max_sum = max(max_sum, cur)
        return max_sum


def test(nums: list[int], k: int) -> int:
    return Solution().maximumSubarraySum(nums, k)


assert test([1, 5, 4, 2, 9, 9, 9], 3) == 15
assert test([4, 4, 4], 3) == 0
assert test([1, 1, 1, 7, 8, 9], 3) == 24
