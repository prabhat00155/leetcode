"""Delete Characters to Make Fancy String
https://leetcode.com/problems/delete-characters-to-make-fancy-string
"""


class Solution:
    def makeFancyString(self, s: str) -> str:
        output = []
        for c in s:
            if len(output) <= 1 or output[-1] != c or output[-2] != c:
                output.append(c)
        return ''.join(output)


def test(s: str) -> str:
    return Solution().makeFancyString(s)


assert test('leeetcode') == 'leetcode'
assert test('aaabaaaa') == 'aabaa'
assert test('aab') == 'aab'
