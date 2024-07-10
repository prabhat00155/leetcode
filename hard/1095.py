"""Find in Mountain Array
https://leetcode.com/problems/find-in-mountain-array
"""


# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
class MountainArray:
    def get(self, index: int) -> int:
        pass

    def length(self) -> int:
        pass


class Solution:
    def findInMountainArray(
        self, target: int, mountain_arr: 'MountainArray'
    ) -> int:
        def find_peak(left, right):
            while left < right:
                mid = left + (right - left) // 2
                if mountain_arr.get(mid) < mountain_arr.get(mid + 1):
                    left = mid + 1
                else:
                    right = mid
            return left

        def binary_search(left, right, target, ascending=True):
            while left <= right:
                mid = left + (right - left) // 2
                mid_value = mountain_arr.get(mid)
                if mid_value == target:
                    return mid
                if ascending:
                    if mid_value < target:
                        left = mid + 1
                    else:
                        right = mid - 1
                else:
                    if mid_value < target:
                        right = mid - 1
                    else:
                        left = mid + 1
            return -1

        size = mountain_arr.length()
        peak = find_peak(0, size - 1)

        # Search in the increasing part
        index = binary_search(0, peak, target, True)
        if index != -1:
            return index

        # Search in the decreasing part
        return binary_search(peak + 1, size - 1, target, False)
