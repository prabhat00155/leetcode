"""Find the Power of K-Size Subarrays I

https://leetcode.com/problems/find-the-power-of-k-size-subarrays-i
"""


class Solution:
    def resultsArray(self, nums: list[int], k: int) -> list[int]:
        if k == 1:
            return nums
        output = []
        is_ascending = True
        i, j = 0, 1
        while i < len(nums) and j < len(nums):
            if j - i + 1 < k:
                is_ascending = is_ascending and nums[j] == nums[j - 1] + 1
            elif is_ascending:
                is_ascending = nums[j] == nums[j - 1] + 1
                output.append(nums[j] if is_ascending else -1)
                i += 1
            else:
                tmp = i + 1
                is_ascending = True
                while tmp <= j:
                    if nums[tmp] != nums[tmp - 1] + 1:
                        is_ascending = False
                        break
                    tmp += 1
                output.append(nums[j] if is_ascending else -1)
                i += 1
            j += 1
        return output


def test(nums: list[int], k: int) -> list[int]:
    return Solution().resultsArray(nums, k)


assert test([1, 2, 3, 4, 3, 2, 5], 3) == [3, 4, -1, -1, -1]
assert test([2, 2, 2, 2, 2], 4) == [-1, -1]
assert test([3, 2, 3, 2, 3, 2], 2) == [-1, 3, -1, 3, -1]
assert test([1], 1) == [1]
assert test([1, 4], 1) == [1, 4]
assert test([1, 3, 4], 2) == [-1, 4]
