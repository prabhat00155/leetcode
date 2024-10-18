"""Count Number of Maximum Bitwise-OR Subsets
https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets
"""


class Solution:
    def countMaxOrSubsets(self, nums: list[int]) -> int:
        maxima, count = 0, 0
        considered = set()
        for n in nums:
            maxima = maxima | n

        def res_count(index, cur, indices):
            nonlocal count
            if cur == maxima and indices not in considered:
                count += 1
                considered.add(indices)
            if index >= len(nums):
                return
            res_count(index+1, cur, indices)
            res_count(index+1, cur | nums[index], indices+(index,))

        res_count(0, 0, ())
        return count


def test(nums: list[int]):
    return Solution().countMaxOrSubsets(nums)


assert test([3, 1]) == 2
assert test([2, 2, 2]) == 7
assert test([3, 2, 1, 5]) == 6
