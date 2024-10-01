"""XOR Operation in an Array
https://leetcode.com/problems/xor-operation-in-an-array
"""


class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        res = 0
        for i in range(n):
            res ^= (start + 2 * i)
        return res


def test(n: int, start: int):
    print(Solution().xorOperation(n, start))


test(5, 0)
test(4, 3)
