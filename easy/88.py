"""Merge Sorted Array
https://leetcode.com/problems/merge-sorted-array/
"""


class Solution:
    def merge(
        self, nums1: list[int], m: int, nums2: list[int], n: int
    ) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        k = m + n - 1
        while i >= 0 and j >= 0:
            if nums2[j] > nums1[i]:
                nums1[k] = nums2[j]
                j -= 1
            else:
                nums1[k] = nums1[i]
                i -= 1
            k -= 1
        while j >= 0:
            nums1[k] = nums2[j]
            k -= 1
            j -= 1


def test(nums1, m, nums2, n):
    print(f'nums1: {nums1}')
    print(f'nums2: {nums2}')
    Solution().merge(nums1, m, nums2, n)
    print(f'Merged: {nums1}')


test([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
test([1], 1, [], 0)
test([0], 0, [1], 1)
