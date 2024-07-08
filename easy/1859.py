"""Sorting the Sentence
https://leetcode.com/problems/sorting-the-sentence
"""


class Solution:
    def sortSentence(self, s: str) -> str:
        output = [None] * len(s.split())
        for w in s.split():
            output[int(w[-1]) - 1] = w[:-1]
        return ' '.join(output)


def test(s):
    print(Solution().sortSentence(s))


test('is2 sentence4 This1 a3')
test('Myself2 Me1 I4 and3')
