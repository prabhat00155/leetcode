"""Edit Distance
https://leetcode.com/problems/edit-distance
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        mapper = [[-1] * len(word2) for _ in word1]

        def min_dist(i, j):
            if j >= len(word2):
                return len(word1) - i
            if i >= len(word1):
                return len(word2) - j
            if mapper[i][j] == -1:
                mapper[i][j] = (
                    min_dist(i+1, j+1) if word1[i] == word2[j]
                    else 1 + min(min_dist(i+1, j+1), min_dist(i+1, j),
                                 min_dist(i, j+1))
                )
            return mapper[i][j]

        return min_dist(0, 0)


def test(word1, word2):
    print(Solution().minDistance(word1, word2))


test('horse', 'ros')
test('intention', 'execution')
