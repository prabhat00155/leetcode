"""Check if The Number is Fascinating
https://leetcode.com/problems/check-if-the-number-is-fascinating
"""


class Solution:
    def isFascinating(self, n: int) -> bool:
        digits = {1, 2, 3, 4, 5, 6, 7, 8, 9}
        for num in [n, 2 * n, 3 * n]:
            while num > 0:
                d = num % 10
                num = num // 10
                if d in digits:
                    digits.remove(d)
                else:
                    return False
        return len(digits) == 0


def test(n: int):
    print(Solution().isFascinating(n))


test(192)
test(100)
