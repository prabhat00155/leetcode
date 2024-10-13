"""Smallest Range Covering Elements from K Lists
https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists
"""


import heapq


class Solution:
    def smallestRange(self, nums: list[list[int]]) -> list[int]:
        min_heap = []
        range_min, range_max = 0, float('inf')
        cur_max = -float('inf')
        for index, arr in enumerate(nums):
            heapq.heappush(min_heap, (arr[0], 0, index))
            cur_max = max(cur_max, arr[0])
        while len(min_heap) == len(nums):
            cur_min = min_heap[0][0]
            if (cur_max - cur_min < range_max - range_min) or (
                    cur_max - cur_min == range_max - range_min
                    and cur_min < range_min):
                range_max, range_min = cur_max, cur_min
            _, offset, index = heapq.heappop(min_heap)
            if offset + 1 < len(nums[index]):
                heapq.heappush(
                        min_heap, (nums[index][offset + 1], offset+1, index))
                cur_max = max(cur_max, nums[index][offset + 1])
        return [range_min, range_max]


def test(nums: list[list[int]]):
    print(Solution().smallestRange(nums))


test([[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]])
test([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
