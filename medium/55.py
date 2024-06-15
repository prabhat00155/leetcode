"""Jump Game
https://leetcode.com/problems/jump-game
"""


class Solution:
    def canJump(self, nums: list[int]) -> bool:
        reach = 0
        for index, value in enumerate(nums):
            if reach < index:
                return False
            reach = max(reach, index+value)
        return reach >= len(nums) - 1


def test(nums):
    print(Solution().canJump(nums))


test([2, 3, 1, 1, 4])
test([3, 2, 1, 0, 4])
