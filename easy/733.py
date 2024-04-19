"""Flood Fill
https://leetcode.com/problems/flood-fill/
"""


class Solution:
    def floodFill(
        self, image: list[list[int]], sr: int, sc: int, color: int
    ) -> list[list[int]]:
        visited = set()

        def fill(sr, sc, colour, original_colour):
            if (
                (sr, sc) in visited or sr < 0 or sr >= len(image)
                or sc < 0 or sc >= len(image[0])
                or image[sr][sc] != original_colour
            ):
                return
            visited.add((sr, sc))
            image[sr][sc] = colour
            fill(sr+1, sc, colour, original_colour)
            fill(sr-1, sc, colour, original_colour)
            fill(sr, sc+1, colour, original_colour)
            fill(sr, sc-1, colour, original_colour)

        if image and 0 <= sr < len(image) and 0 <= sc < len(image[0]):
            fill(sr, sc, color, image[sr][sc])

        return image


def test(image, sr, sc, colour):
    print(Solution().floodFill(image, sr, sc, colour))


test([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2)
test([[0, 0, 0], [0, 0, 0]], 0, 0, 0)
