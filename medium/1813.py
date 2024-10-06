"""Sentence Similarity III
https://leetcode.com/problems/sentence-similarity-iii
"""


class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        if sentence1 == sentence2:
            return True

        def find_missing_components(words1, words2):
            i, j = 0, 0
            missing_components = 0
            continuation = False
            while i < len(words1) or j < len(words2):
                if i >= len(words1) or j >= len(words2):
                    if j < len(words2):
                        return False
                    missing_components = (
                        missing_components if continuation
                        else missing_components + 1
                    )
                    break
                elif words1[i] == words2[j]:
                    i += 1
                    j += 1
                    continuation = False
                else:
                    if not continuation:
                        missing_components += 1
                        continuation = True
                    i += 1
            return missing_components

        words1 = sentence1.split()
        words2 = sentence2.split()
        if len(words2) > len(words1):
            words1, words2 = words2, words1

        return (
            find_missing_components(words1, words2) == 1
            or find_missing_components(
                list(reversed(words1)), list(reversed(words2))) == 1
        )


def test(sentence1: str, sentence2: str):
    print(Solution().areSentencesSimilar(sentence1, sentence2))


test('My name is Haley', 'My Haley')
test('of', 'A lot of words')
test('Eating right now', 'Eating')
test('Luky', 'Lucccky')
test('A', 'a A b A')
test('TjZ ScAi m xz PNWaKigqqY p IyJ B rok',
     'TjZ ScAi m LlbJhCf gL u m R pZpiH mSk a og xz PNWaKigqqY p IyJ B rok')
