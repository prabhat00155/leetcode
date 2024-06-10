"""Jump Game II
https://leetcode.com/problems/jump-game-ii
"""


class Solution:
    def jump(self, nums: list[int]) -> int:
        mapper = [float('inf') for _ in nums]

        def min_jump(nums, i):
            if i == len(nums) - 1:
                return 0
            if i >= len(nums):
                return float('inf')
            if mapper[i] != float('inf'):
                return mapper[i]
            for j in range(1, nums[i]+1):
                mapper[i] = min(mapper[i], 1 + min_jump(nums, i+j))
            return mapper[i]

        return min_jump(nums, 0)


def test(nums):
    print(Solution().jump(nums))


test([2, 3, 1, 1, 4])
test([2, 3, 0, 1, 4])
