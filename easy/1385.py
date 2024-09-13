"""Find the Distance Value Between Two Arrays
https://leetcode.com/problems/find-the-distance-value-between-two-arrays
"""


class Solution:
    def findTheDistanceValue(
        self, arr1: list[int], arr2: list[int], d: int
    ) -> int:
        total, found = 0, True
        for e1 in arr1:
            found = True
            for e2 in arr2:
                if abs(e1 - e2) <= d:
                    found = False
                    break
            total += int(found)
        return total


def test(arr1: list[int], arr2: list[int], d: int):
    print(Solution().findTheDistanceValue(arr1, arr2, d))


test([4, 5, 8], [10, 9, 1, 8], 2)
test([1, 4, 2, 3], [-4, -3, 6, 10, 20, 30], 3)
test([2, 1, 100, 3], [-5, -2, 10, -3, 7], 6)
