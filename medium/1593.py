"""Split a String Into the Max Number of Unique Substrings
https://leetcode.com/problems/split-a-string-into-the-max-number-of-unique-substrings
"""


class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        maxima = 0

        def split(cur_res, cur, index):
            if index >= len(s):
                if cur not in cur_res:
                    cur_res.add(cur)
                    nonlocal maxima
                    maxima = max(len(cur_res), maxima)
                return
            if cur and cur not in cur_res:
                cur_res2 = set(cur_res)
                cur_res2.add(cur)
                split(cur_res2, s[index], index+1)
            split(cur_res, f'{cur}{s[index]}', index+1)

        split(set(), '', 0)
        return maxima


def test(s: str) -> int:
    return Solution().maxUniqueSplit(s)


assert test('ababccc') == 5
assert test('aba') == 2
assert test('aa') == 1
