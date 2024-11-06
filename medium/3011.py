"""Find if Array Can Be Sorted

https://leetcode.com/problems/find-if-array-can-be-sorted
"""


class Solution:
    def canSortArray(self, nums: list[int]) -> bool:
        mapper = {}

        def set_bits(num):
            if num not in mapper:
                count = 0
                while num > 0:
                    if num & 1 == 1:
                        count += 1
                    num >>= 1
                mapper[num] = count
            return mapper[num]

        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] > nums[j]:
                    if set_bits(nums[i]) != set_bits(nums[j]):
                        return False
                    nums[i], nums[j] = nums[j], nums[i]
        return True


def test(nums: list[int]) -> bool:
    return Solution().canSortArray(nums)


assert test([8, 4, 2, 30, 15])
assert test([1, 2, 3, 4, 5])
assert not test([3, 16, 8, 4, 2])
assert not test([2, 28, 9])
