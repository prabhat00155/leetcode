"""Intersection of Two Arrays II
https://leetcode.com/problems/intersection-of-two-arrays-ii
"""


from collections import Counter


class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        output = []
        freq1 = Counter(nums1)
        for num in nums2:
            if num in freq1:
                output.append(num)
                freq1[num] -= 1
                if freq1[num] == 0:
                    del freq1[num]
        return output


def test(nums1: list[int], nums2: list[int]):
    print(Solution().intersect(nums1, nums2))


test([1, 2, 2, 1], [2, 2])
test([4, 9, 5], [9, 4, 9, 8, 4])
