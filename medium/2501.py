"""Longest Square Streak in an Array
https://leetcode.com/problems/longest-square-streak-in-an-array
"""


class Solution:
    def longestSquareStreak(self, nums: list[int]) -> int:
        nums_set = set(nums)

        def streak(n):
            count = 0
            while n * n in nums_set:
                count += 1
                n = n * n
            return count

        max_streak = 0
        for n in nums:
            max_streak = max(max_streak, streak(n))
        return -1 if max_streak == 0 else max_streak + 1


def test(nums: list[int]) -> int:
    return Solution().longestSquareStreak(nums)


assert test([4, 3, 6, 16, 8, 2]) == 3
assert test([2, 3, 5, 6, 7]) == -1
