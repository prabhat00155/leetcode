"""Check If String Is a Prefix of Array
https://leetcode.com/problems/check-if-string-is-a-prefix-of-array
"""


class Solution:
    def isPrefixString(self, s: str, words: list[str]) -> bool:
        i = 0
        for word in words:
            for c in word:
                if i >= len(s) or s[i] != c:
                    return False
                i += 1
            if i >= len(s):
                break
        return i == len(s)


def test(s, words):
    print(Solution().isPrefixString(s, words))


test('iloveleetcode', ['i', 'love', 'leetcode', 'apples'])
test('iloveleetcode', ['apples', 'i', 'love', 'leetcode'])
