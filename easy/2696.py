"""Minimum String Length After Removing Substrings
https://leetcode.com/problems/minimum-string-length-after-removing-substrings
"""


class Solution:
    def minLength(self, s: str) -> int:
        stk = []
        for c in s:
            if len(stk) == 0 or c not in ('B', 'D'):
                stk.append(c)
            elif (stk[-1] == 'A' and c == 'B') or (
                  stk[-1] == 'C' and c == 'D'):
                stk.pop()
            else:
                stk.append(c)
        return len(stk)


def test(s: str):
    print(Solution().minLength(s))


test('ABFCACDB')
test('ACBBD')
test('CCCCDDDD')
test('ABG')
test('CABDCABDAB')
test('CCDAABBDCD')
