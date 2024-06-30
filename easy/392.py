"""Is Subsequence
https://leetcode.com/problems/is-subsequence
"""


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)


def test(s, t):
    print(Solution().isSubsequence(s, t))


test('abc', 'ahbgdc')
test('axc', 'ahbgdc')