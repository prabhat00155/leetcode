"""Uncommon Words from Two Sentences
https://leetcode.com/problems/uncommon-words-from-two-sentences
"""


from collections import Counter


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
        freq1 = Counter(s1.split())
        freq2 = Counter(s2.split())
        output = []

        for k, v in freq1.items():
            if k not in freq2 and v == 1:
                output.append(k)
        for k, v in freq2.items():
            if k not in freq1 and v == 1:
                output.append(k)
        return output


def test(s1: str, s2: str):
    print(Solution().uncommonFromSentences(s1, s2))


test('this apple is sweet', 'this apple is sour')
test('apple apple', 'banana')
