"""Maximum Swap
https://leetcode.com/problems/maximum-swap
"""


class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = []
        n, index = num, 0
        while n > 0:
            digits.append((n % 10, index))
            index += 1
            n = n // 10
        digits_sorted = sorted(digits)
        res = 0
        i, j = len(digits_sorted) - 1, len(digits) - 1
        while i > 0 and j >= 0:
            if digits_sorted[i][0] == digits[j][0]:
                i -= 1
                j -= 1
            elif digits_sorted[i - 1][0] == digits_sorted[i][0]:
                i -= 1
            else:
                loc1 = digits[j][1]
                loc2 = digits_sorted[i][1]
                digits[loc1], digits[loc2] = digits[loc2], digits[loc1]
                break
        for d, _ in reversed(digits):
            res = res * 10 + d
        return res


def test(num: int):
    return Solution().maximumSwap(num)


assert test(2736) == 7236
assert test(9973) == 9973
assert test(1993) == 9913
assert test(98368) == 98863
