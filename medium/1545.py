"""Find Kth Bit in Nth Binary String
https://leetcode.com/problems/find-kth-bit-in-nth-binary-string
"""


class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def invert(s):
            output = []
            for c in s:
                output.append('0' if c == '1' else '1')
            return ''.join(output)

        def fetch_string(n):
            if n == 1:
                return '0'
            prev = fetch_string(n-1)
            inverted = invert(prev)
            return f'{prev}1{inverted[::-1]}'

        return fetch_string(n)[k - 1]


def test(n: int, k: int):
    return Solution().findKthBit(n, k)


assert test(3, 1) == '0'
assert test(4, 11) == '1'
