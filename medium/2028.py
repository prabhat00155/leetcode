"""Find Missing Observations
https://leetcode.com/problems/find-missing-observations
"""


class Solution:
    def missingRolls(self, rolls: list[int], mean: int, n: int) -> list[int]:
        n_total = mean * (len(rolls) + n) - sum(rolls)
        output = []
        if n_total > 6 * n:
            return output
        while n_total > 0 and n > 0:
            each = n_total // n
            if each == 0:
                return []
            if n > 1:
                output.append(each)
                n_total -= each
            elif n_total <= 6:
                output.append(n_total)
                n_total = 0
            n -= 1
        return output if n_total == 0 and n == 0 else []


def test(rolls, mean, n):
    print(Solution().missingRolls(rolls, mean, n))


test([3, 2, 4, 3], 4, 2)
test([1, 5, 6], 3, 4)
test([1, 2, 3, 4], 6, 4)
