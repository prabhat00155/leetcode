"""Ransom Note
https://leetcode.com/problems/ransom-note
"""


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq = {}
        for c in magazine:
            freq[c] = freq.get(c, 0) + 1
        for c in ransomNote:
            if c not in freq or freq[c] == 0:
                return False
            freq[c] -= 1
        return True


def test(ranson_note, magazine):
    print(Solution().canConstruct(ranson_note, magazine))


test('a', 'b')
test('aa', 'ab')
test('aa', 'aab')
