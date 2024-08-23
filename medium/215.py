"""Kth Largest Element in an Array
https://leetcode.com/problems/kth-largest-element-in-an-array
"""


import heapq


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heap = []
        for num in nums:
            if len(heap) < k:
                heapq.heappush(heap, num)
            else:
                heapq.heappushpop(heap, num)
        return heap[0]


def test(nums: list[int], k: int):
    print(Solution().findKthLargest(nums, k))


test([3, 2, 1, 5, 6, 4], 2)
test([3, 2, 3, 1, 2, 4, 5, 5, 6], 4)
