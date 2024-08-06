"""Minimum Number of Pushes to Type Word II
https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii
"""


class Solution:
    def minimumPushes(self, word: str) -> int:
        letters = {}
        for c in word:
            letters[c] = letters.get(c, 0) + 1
        coef, pushes, count = 1, 0, 0
        for k, v in sorted(letters.items(), key=lambda x: x[1], reverse=True):
            pushes += coef * v
            count += 1
            if count % 8 == 0:
                coef += 1
        return pushes


def test(word: str):
    print(Solution().minimumPushes(word))


test('abcde')
test('xyzxyzxyzxyz')
test('aabbccddeeffgghhiiiiii')
