"""4 Sum
https://leetcode.com/problems/4sum
"""


class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        soln = set()
        for i1, n1 in enumerate(nums):
            for i2 in range(i1+1, len(nums)):
                n2 = nums[i2]
                required = target - (n1 + n2)
                start = i2 + 1
                end = len(nums) - 1
                while start < end:
                    val = nums[start] + nums[end]
                    if val == required:
                        soln.add(tuple([n1, n2, nums[start], nums[end]]))
                        end -= 1
                    elif val < required:
                        start += 1
                    else:
                        end -= 1
        return list(map(lambda x: list(x), soln))


def test(arr, target):
    print(Solution().fourSum(arr, target))


test([1, 0, -1, 0, -2, 2], 0)
test([2, 2, 2, 2, 2], 8)
