"""Circular Sentence

https://leetcode.com/problems/circular-sentence
"""


class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        if sentence[0] != sentence[-1]:
            return False
        sentences = sentence.split()
        for i in range(1, len(sentences)):
            if sentences[i - 1][-1] != sentences[i][0]:
                return False
        return True


def test(sentence: str) -> bool:
    return Solution().isCircularSentence(sentence)


assert test('leetcode exercises sound delightful')
assert test('eetcode')
assert not test('Leetcode is cool')
