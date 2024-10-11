"""Three Divisors
https://leetcode.com/problems/three-divisors
"""


class Solution:
    def isThree(self, n: int) -> bool:
        count = 1
        for i in range(1, 1+n//2):
            if n % i == 0:
                count += 1
        return count == 3


def test(n: int):
    print(Solution().isThree(n))


test(2)
test(4)
test(1)
