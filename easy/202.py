"""Happy Number
https://leetcode.com/problems/happy-number
"""


class Solution:
    def isHappy(self, n: int) -> bool:
        def sum_of_squares(n):
            total = 0
            while n > 0:
                total += (n % 10) * (n % 10)
                n = n // 10
            return total

        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = sum_of_squares(n)
        return n == 1


def test(n: int):
    print(Solution().isHappy(n))


test(19)
test(2)
