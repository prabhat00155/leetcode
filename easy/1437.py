"""Check If All 1's Are at Least Length K Places Away
https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away
"""


class Solution:
    def kLengthApart(self, nums: list[int], k: int) -> bool:
        last_seen = -1
        for index, value in enumerate(nums):
            if value == 1:
                if last_seen != -1 and index - last_seen - 1 < k:
                    return False
                last_seen = index
        return True


def test(nums, k):
    print(Solution().kLengthApart(nums, k))


test([1, 0, 0, 0, 1, 0, 0, 1], 2)
test([1, 0, 0, 1, 0, 1], 2)
