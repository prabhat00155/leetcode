"""Palindrome Partitioning
https://leetcode.com/problems/palindrome-partitioning
"""


class Solution:
    def partition(self, s: str) -> list[list[str]]:
        output = []

        def is_palindrome(s):
            return s == s[::-1]

        def pal_partition(s, cur):
            if not s:
                output.append(cur.copy())
            for i in range(1, len(s)+1):
                if is_palindrome(s[:i]):
                    cur.append(s[:i])
                    pal_partition(s[i:], cur)
                    cur.pop()

        pal_partition(s, [])
        return output


def test(s):
    print(Solution().partition(s))


test('aab')
test('a')
