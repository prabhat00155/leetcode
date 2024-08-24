"""Count Special Quadruplets
https://leetcode.com/problems/count-special-quadruplets
"""


class Solution:
    def countQuadruplets(self, nums: list[int]) -> int:
        total = 0
        for i in range(len(nums)-3):
            for j in range(i+1, len(nums)-2):
                for k in range(j+1, len(nums)-1):
                    for m in range(k+1, len(nums)):
                        if nums[i] + nums[j] + nums[k] == nums[m]:
                            total += 1
        return total


def test(nums: list[int]):
    print(Solution().countQuadruplets(nums))


test([1, 2, 3, 6])
test([3, 3, 6, 4, 5])
test([1, 1, 1, 3, 5])
test([28, 8, 49, 85, 37, 90, 20, 8])
