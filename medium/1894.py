"""Find the Student that Will Replace the Chalk
https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk
"""


class Solution:
    def chalkReplacer(self, chalk: list[int], k: int) -> int:
        rem = k % sum(chalk)
        cur = 0
        for index, val in enumerate(chalk):
            cur += val
            if rem < cur:
                return index


def test(chalk: list[int], k: int):
    print(Solution().chalkReplacer(chalk, k))


test([5, 1, 5], 22)
test([3, 4, 1, 2], 25)
