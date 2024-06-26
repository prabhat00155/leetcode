"""Palindrome Partitioning II
https://leetcode.com/problems/palindrome-partitioning-ii
"""


class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        is_palindrome = [[False] * n for _ in s]

        for length in range(1, n+1):
            for i in range(n-length+1):
                j = i + length - 1
                if length == 1:
                    is_palindrome[i][j] = True
                elif length == 2:
                    is_palindrome[i][j] = s[i] == s[j]
                else:
                    is_palindrome[i][j] = (s[i] == s[j]
                                           and is_palindrome[i + 1][j - 1])

        cuts = [float('inf')] * n
        for i in range(n):
            if is_palindrome[0][i]:
                cuts[i] = 0
            else:
                for j in range(i):
                    if is_palindrome[j+1][i]:
                        cuts[i] = min(cuts[i], cuts[j]+1)
        return cuts[-1]


def test(s):
    print(Solution().minCut(s))


test('aab')
test('a')
test('ab')
