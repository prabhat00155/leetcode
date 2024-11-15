"""Shortest Subarray to be Removed to Make Array Sorted

https://leetcode.com/problems/shortest-subarray-to-be-removed-to-make-array-sorted
"""


class Solution:
    def findLengthOfShortestSubarray(self, arr: list[int]) -> int:
        start = 0
        while start < len(arr) - 1 and arr[start + 1] >= arr[start]:
            start += 1
        if start == len(arr) - 1:
            return 0
        end = len(arr) - 1
        while end > 0 and arr[end] >= arr[end - 1]:
            end -= 1

        result = min(len(arr)-start-1, end)

        i, j = 0, end
        while i <= start and j < len(arr):
            if arr[i] <= arr[j]:
                result = min(result, j-i-1)
                i += 1
            else:
                j += 1
        return result


def test(arr: list[int]) -> int:
    return Solution().findLengthOfShortestSubarray(arr)


assert test([1, 2, 3, 10, 4, 2, 3, 5]) == 3
assert test([5, 4, 3, 2, 1]) == 4
assert test([1, 2, 3]) == 0
assert test([1, 2, 3, 10, 0, 7, 8, 9]) == 2
assert test([1, 2, 3, 10, 0, 2, 7, 8, 9]) == 3
