"""Maximal Score After Applying K Operations
https://leetcode.com/problems/maximal-score-after-applying-k-operations
"""


import math
import heapq


class Solution:
    def maxKelements(self, nums: list[int], k: int) -> int:
        max_heap = []
        score = 0

        for n in nums:
            heapq.heappush(max_heap, -n)

        while k > 0:
            top = -heapq.heappop(max_heap)
            score += top
            top = math.ceil(top/3)
            heapq.heappush(max_heap, -top)
            k -= 1
        return score


def test(nums: list[int], k: int):
    print(Solution().maxKelements(nums, k))


test([10, 10, 10, 10, 10], 5)
test([1, 10, 3, 3, 3], 3)
