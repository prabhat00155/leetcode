"""Defuse the Bomb

https://leetcode.com/problems/defuse-the-bomb
"""


from collections import deque


class Solution:
    def decrypt(self, code: list[int], k: int) -> list[int]:

        def handle_next():
            output = []
            i, count, cur = 1, 0, 0
            while count < k:
                cur += code[i]
                count += 1
                i = (i + 1) % len(code)
            output.append(cur)
            for ind in range(1, len(code)):
                val = code[ind]
                output.append(output[-1]-val+code[(ind+k) % len(code)])
            return output

        def handle_prev():
            output = deque()
            k2 = abs(k)
            i, count, cur = len(code) - 2, 0, 0
            while count < k2:
                cur += code[i]
                count += 1
                i = (i - 1) % len(code)
            output.append(cur)
            for ind in range(len(code)-2, -1, -1):
                val = code[ind]
                output.appendleft(output[0]-val+code[(ind-k2) % len(code)])
            return list(output)

        if k == 0:
            return [0] * len(code)
        return handle_next() if k > 0 else handle_prev()


def test(code: list[int], k: int) -> list[int]:
    return Solution().decrypt(code, k)


assert test([5, 7, 1, 4], 3) == [12, 10, 16, 13]
assert test([1, 2, 3, 4], 0) == [0, 0, 0, 0]
assert test([2, 4, 9, 3], -2) == [12, 5, 6, 13]
