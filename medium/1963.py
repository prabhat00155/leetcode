"""Minimum Number of Swaps to Make the String Balanced
https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced
"""


class Solution:
    def minSwaps(self, s: str) -> int:
        i, j = 0, len(s) - 1
        n_open, n_close = 0, 0
        swaps = 0
        while i < j:
            if s[i] == '[':
                i += 1
                n_open += 1
            if s[j] == ']':
                j -= 1
                n_close += 1
            if s[i] == ']' and n_open == 0 and s[j] == '[' and n_close == 0:
                swaps += 1
                n_open += 1
                n_close += 1
                i += 1
                j -= 1
            else:
                if s[i] == ']' and n_open > 0:
                    n_open -= 1
                    i += 1
                if s[j] == '[' and n_close > 0:
                    n_close -= 1
                    j -= 1
        return swaps


def test(s: str):
    print(Solution().minSwaps(s))


test('][][')
test(']]][[[')
test('[]')
test('[[[]]]][][]][[]]][[[')
