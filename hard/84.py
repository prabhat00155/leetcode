"""Largest Rectange in Histogram
https://leetcode.com/problems/largest-rectangle-in-histogram
"""


class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = []
        max_area = 0
        index = 0

        while index < len(heights):
            if not stack or heights[index] >= heights[stack[-1]]:
                stack.append(index)
                index += 1
            else:
                area = heights[stack.pop()] * (
                        index - stack[-1] - 1 if stack else index)
                max_area = max(max_area, area)

        while stack:
            area = heights[stack.pop()] * (
                    index - stack[-1] - 1 if stack else index)
            max_area = max(max_area, area)

        return max_area


def test(heights):
    print(Solution().largestRectangleArea(heights))


test([2, 1, 5, 6, 2, 3])
test([2, 4])
