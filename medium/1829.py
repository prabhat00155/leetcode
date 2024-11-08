"""Maximum XOR for Each Query
https://leetcode.com/problems/maximum-xor-for-each-query
"""


class Solution:
    def getMaximumXor(self, nums: list[int], maximumBit: int) -> list[int]:
        output = []
        val = 2 ** maximumBit - 1
        xor = nums[0]
        for i in range(1, len(nums)):
            xor = xor ^ nums[i]
        output.append(xor ^ val)
        last = len(nums) - 1
        while len(output) < len(nums):
            output.append(output[-1] ^ nums[last])
            last -= 1
        return output


def test(nums: list[int], maximum_bit: int) -> list[int]:
    return Solution().getMaximumXor(nums, maximum_bit)


assert test([0, 1, 1, 3], 2) == [0, 3, 2, 3]
assert test([2, 3, 4, 7], 3) == [5, 2, 6, 5]
assert test([0, 1, 2, 2, 5, 7], 3) == [4, 3, 6, 4, 6, 7]
