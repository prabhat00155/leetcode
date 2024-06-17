"""Container With Most Water
https://leetcode.com/problems/container-with-most-water
"""


class Solution:
    def maxArea(self, height: list[int]) -> int:
        i = 0
        j = len(height) - 1
        max_area = 0

        while i < j:
            area = min(height[i], height[j]) * (j - i)
            max_area = max(max_area, area)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return max_area


def test(height):
    print(Solution().maxArea(height))


test([1, 8, 6, 2, 5, 4, 8, 3, 7])
test([1, 1])
